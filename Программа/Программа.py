#datacode = [401, 500, 200, 404, 503, 200, 200, 403, 777, 500, 200, 404, 200, 503, 401, 200, 500, 777, 777, 777]
datacode = list(map(int, input(":").split()))
normal = 0 #код 200
access_error = 0 #код 401 и 403
not_found = 0 #код 404
internal_server_error = 0 #код 500
server_unavailable = 0 #код 503
unknown_error = 0 #для неизвестных кодов

for i in datacode: #перебор списка кодов
    if i == 200:
        normal += 1
    elif i == 401 or i == 403:
        access_error += 1
    elif i == 404:
        not_found += 1
    elif i == 500:
        internal_server_error += 1
    elif i == 503:
        server_unavailable += 1
    else:
        unknown_error += 1
print("Успешно код 200 - ", normal, "\nПроблема Доступа код 401 и 403 - ", access_error, "\nРесурс не найден код 404 - ", not_found, "\nКритическая ошибка код 500 - ", internal_server_error, "\nКритическая ошибка код 503 - ", server_unavailable, "\nНеизвестные ошибки - ", unknown_error)

critical_error = internal_server_error + server_unavailable
print("Общее количество критических ошибок - ", critical_error)

if critical_error <= 2:
    print("Состояние: Cтабильно")
elif critical_error <= 5:
    print("Состояние: Внимание")
else:
    print("Состояние: Критическое")