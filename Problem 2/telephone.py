def telephone():
    phone_number = int(input())
    phone_acode = str(phone_number // 10000000)
    phone_middle = str((phone_number // 10000) % 1000)
    phone_end = str(phone_number % 10000)
    print('('+phone_acode+') '+phone_middle+'-'+phone_end)
if __name__ == "__main__":
    telephone()