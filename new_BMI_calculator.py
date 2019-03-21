import json
global login
global password
login = False
password = False
#Словарь логинов и паролей


while True:
    
    
    

    #логин
    def auth():
        global login
        global password
        
        login = str(input('Введите логин: '))
        password = str(input('Введите пароль: '))
    
    #регистрация
    def register():
        log = str(input('Выберите логин: '))
        passw = str(input('Выберите пароль: '))
        with open ('logs_and_passwords_bmi.txt', 'r') as f:
            login_list = json.load(f)
        if log in login_list:
            print('Выберите другой логин')
            return register()
        else:
            login_list[log] = passw
            with open('logs_and_passwords_bmi.txt', 'w') as f:
                json.dump(login_list, f, indent = 4)
            print('Пользователь добавлен')

        

    #проверка авторизации

    def auth_check(func):
        def wrapper():
            with open ('logs_and_passwords_bmi.txt', 'r') as f:
                login_list = json.load(f)
            if login in login_list and login_list[login] == password:
                func()
            else:
                print('Неверный логин и пароль.', '\n',  
                    '1 - Авторизируйтесь или 2 - зарегистрируйтесь.')
                c = int(input('выбор'))
                if c == 1:
                    auth()
                elif c == 2:
                    register()
        return wrapper
        
        
           

    

            

    #Список пользователей
    
    #Построение динамического графика
    def graph(bmi):
        graphic = '17.5'
        for i in range (17, 40):
            if i != round(bmi):
                graphic += '__'
            elif i == round(bmi):
                graphic += str(bmi)
        print(graphic + '40')

    def main():
        #Калькулятор BMI fdff
        print('Выберите действие', '\n', '1 Вывести список пользователей', '\n', '2 Добавить пользователя', \
            '\n', '3 Удалить пользователя', '\n', '4 Выбрать пользователя', '\n', '5 Рассчет BMI', '\n', '6 Зарегистрироваться', 
                '\n', '7 Авторизироваться')
        choose = int(input('Введите действие: '))
        if choose == 1:
            list_of_users()
        elif choose == 2:
            add_user()
        elif choose == 3:
            delete_user()
        elif choose == 4:
            choose_user()
        elif choose == 5:
            raschet_bmi()
        elif choose == 6:
            register()   
        elif choose == 7:
            auth()
            
    #Вывести список пользователей
    @auth_check
    def list_of_users():
        with open ('user_list_bmi.txt', 'r') as f:
            user_list = json.load(f)
        for i in user_list:
            print(i)

    #Добавить пользователя
    @auth_check
    def add_user():
        n = str(input('Введите имя: '))
        a = int(input('Введите возраст: '))
        h = float(input('Введите рост: '))
        w = float(input('Введите вес: '))
        with open ('user_list_bmi.txt', 'r') as f:
            user_list = json.load(f)
        user_list[n] = {
            'name' : n,
            'age' : a,
            'height' : h,
            'weight' : w,
        }
        with open ('user_list_bmi.txt', 'w') as f:
            json.dump(user_list, f, indent=4)
        

    #Удалить пользователя
    @auth_check
    def delete_user():
        n = str(input('Введите имя пользователя которого хотите удалить: '))
        with open ('user_list_bmi.txt', 'r') as f:
            user_list = json.load(f)
        del(user_list[n])
        with open ('user_list_bmi.txt', 'w') as f:
            json.dump(user_list, f, indent=2)
        
        
      
        

    #Выбрать пользователя
    @auth_check
    def choose_user():
        n = str(input('Введите имя пользователя: '))
        with open ('user_list_bmi.txt', 'r') as f:
            user_list = json.load(f)
        if n not in user_list:
            print('Нет такого пользователя')
        else:
        #Рассчет BMI
            
            bmi = round(user_list[n]['weight'] / user_list[n]['height']**2, 1)

        #Вывод
            print('Уважаемая(й) {}'. format(n),'\n','Ваш возраст: {}'. format(user_list[n]['age']),'\n', \
                'Ваш рост: {}'.format(user_list[n]['height']),'\n','Ваш вес: {}'. format(user_list[n]['weight']),'\n','Ваш BMI: {}'. format(bmi))

            if bmi <= 17.5:
                print('Анорексия. Риск для здоровья выскоий. Рекомендуется повышение веса.')
                print('Значение вне графика')
            elif bmi >= 17.6 and bmi <= 25.9:
                print('Норма. Риска для здоровья нет.')
                graph(bmi)
            elif bmi >= 26 and bmi <= 27.9:
                print('Избыток веса. Риск для здоровья повышенный. Рекомендуется похудение.')
                graph(bmi)
            elif bmi >= 28 and bmi <= 30.9:
                print('Ожирение I степени. Риск для здоровья повышенный. Рекомендуется снижение массы тела.')
                graph(bmi)
            elif bmi >= 31 and bmi <= 35.9:
                print('Ожирение II степени. Риск для здоровья высокий. Настоятельно рекомендуется снижение массы тела.')
                graph(bmi)
            elif bmi >= 36 and bmi <= 40.9:
                print('Ожирение III степени. Риск для здоровья очень выскоий. Настоятельно рекомендуется снижение массы тела.')
                graph(bmi)
            else:
                print('Ожирение IV степени. Риск для здоровья чрезвычайно высокий. Необходимо немедленное снижение массы тела.')
                print('Значение вне графика')

    @auth_check
    def raschet_bmi():

        name = str(input('Введите имя:'))
        age = int(input('Введите возраст:'))
        height = float(input('Введите рост в метрах:'))
        weight = float(input('Введите вес в кг:'))

        #Рассчет BMI

        bmi = round(weight / height**2, 1)

        #Вывод
        print('Уважаемая(й) {}'. format(name),'\n','Ваш возраст: {}'. format(age),'\n', \
        'Ваш рост: {}'.format(height),'\n','Ваш вес: {}'. format(weight),'\n','Ваш BMI: {}'. format(bmi))

        if bmi <= 17.5:
            print('Анорексия. Риск для здоровья выскоий. Рекомендуется повышение веса.')
            print('Значение вне графика')
            
        elif bmi >= 17.6 and bmi <= 25.9:
            print('Норма. Риска для здоровья нет.')
            graph(bmi)
        elif bmi >= 26 and bmi <= 27.9:
            print('Избыток веса. Риск для здоровья повышенный. Рекомендуется похудение.')
            graph(bmi)
        elif bmi >= 28 and bmi <= 30.9:
            print('Ожирение I степени. Риск для здоровья повышенный. Рекомендуется снижение массы тела.')
            graph(bmi)
        elif bmi >= 31 and bmi <= 35.9:
            print('Ожирение II степени. Риск для здоровья высокий. Настоятельно рекомендуется снижение массы тела.')
            graph(bmi)
        elif bmi >= 36 and bmi <= 40.9:
            print('Ожирение III степени. Риск для здоровья очень выскоий. Настоятельно рекомендуется снижение массы тела.')
            graph(bmi)
        else:
            print('Ожирение IV степени. Риск для здоровья чрезвычайно высокий. Необходимо немедленное снижение массы тела.')
            print('Значение вне графика')
    
    main()    
    