login = str(input('Введите логин: '))
password = str(input('Введите пароль: '))
while True:
    
    #Словарь логинов и паролей
    login_list = {
        'qwerty' : '1234'
    }
    

    #логин
    def auth():
        global login
        global password
        
        login = str(input('Введите логин: '))
        password = str(input('Введите пароль: '))
    


    #проверка авторизации

    def auth_check(func):
        if login in login_list and login_list[login] == password:
            func()
        else:
            auth()

    

            

    #Список пользователей
    user_list = {
        'Василий Петрович' : {
            'name' : 'Василий Петрович',
            'age' : 45,
            'height' : 1.85,
            'weight' : 78,
        },
        'Ольга Васильевна' : {
            'name' : 'Ольга Васильевна',
            'age' : 36,
            'height' : 1.70,
            'weight' : 63,
        }
    }
    #Построение динамического графика
    def graph(bmi):
        graphic = '17.5'
        for i in range (17, 40):
            if i != round(bmi):
                graphic += '__'
            elif i == round(bmi):
                graphic += str(bmi)
        print(graphic + '40')


    #Вывести список пользователей
    
    def list_of_users():
        print(user_list.keys())

    #Добавить пользователя
    
    def add_user():
        n = str(input('Введите имя: '))
        a = int(input('Введите возраст: '))
        h = float(input('Введите рост: '))
        w = float(input('Введите вес: '))
        user_list[n] = {
            'name' : n,
            'age' : a,
            'height' : h,
            'weight' : w,
        }

    #Удалить пользователя
    
    def delete_user():
        n = str(input('Введите имя пользователя которого хотите удалить: '))
        del(user_list[n])
        
        
        

    #Выбрать пользователя
    
    def choose_user():
        n = str(input('Введите имя пользователя: '))
        
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
    
    @auth_check    
    def main():
        #Калькулятор BMI fdff
        print('Выберите действие', '\n', '1 Вывести список пользователей', '\n', '2 Добавить пользователя', \
            '\n', '3 Удалить пользователя', '\n', '4 Выбрать пользователя', '\n', '5 Рассчет BMI')
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