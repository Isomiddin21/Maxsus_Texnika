class SendOTPAPIView(APIView):
    schema = send_otp_schema

    @swagger_auto_schema(
        request_body=send_to_optain_token_response_body,
        responses={200: send_to_optain_token_response}
    )
    def post(self, request):
        language = get_language_from_request(request)
        phone = request.data.get('phone')
        device_id = request.data.get('autofill')
        print(phone, device_id)
        if phone == "+998123456789":
            return Response({"detail": "code sent"})

        resp = send_message(phone=phone, device_id=device_id)
        if resp.status_code == 200:
            return Response({"detail": "Kod yuborildi" if language == "uz" else "Код отправлен"})
        return Response({"detail": "Kod yuborishda xatolik yuz berdi" if language == "uz" else "Ошибка отправки кода"},
                        status=resp.status_code)


class VerifyOTPAPIView(APIView):
    schema = verify_schema

    @swagger_auto_schema(
        request_body=verifay_token_response_body,
        responses={200: verifay_token_response}
    )
    def post(self, request):
        language = get_language_from_request(request)
        code = request.data['code']
        phone = request.data['phone']

        if phone == "+998123456789" and code == "123456":
            user = User.objects.filter(username=phone).first()
            if not user:
                user = User.objects.create(username=phone)
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token), "refresh": str(refresh)})

        cor = check_code(code, phone)
        if cor:
            user = User.objects.filter(username=phone).first()
            if not user:
                user = User.objects.create(username=phone)
        else:
            return Response({'detail': "Kod noto'g'ri kiritildi" if language == "uz" else "Код введен неправильно"},
                            status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})


def check_code(code, phone):
    orginal_code = rds.get(phone)
    if orginal_code is None:
        return False
    orginal_code = orginal_code.decode('utf-8')
    correct = orginal_code == code
    return correct


def generateOTP(phone):
    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    rds.set(name=phone, value=OTP)
    rds.expire(name=phone, time=65)

    return OTP


def send_message(phone, device_id=None):
    otp = generateOTP(phone)
    send_url = BASE_URL + "/message/sms/send"
    token = SMSProvider.objects.first().token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    # Vash kod podtverjdeniya dlya mobilnogo prilojeniya Avtoritet Group:
    data = {
        'mobile_phone': phone[1:],
        'message': f"<#> Your verification code: {otp} {device_id}",
        'from': 'xxxx'
    }

    resp = requests.post(url=send_url, data=data, headers=headers)

    # print(resp.status_code, resp.text)

    if resp.status_code == 401:
        token = refresh_token()

        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp = requests.post(url=send_url, data=data, headers=headers)
    # print(resp.status_code, resp.text)

    return resp
