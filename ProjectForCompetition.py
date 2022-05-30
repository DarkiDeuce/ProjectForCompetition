import telebot
from random import randint, choice
from telebot import types

hp_monster = 0
cost = 0
recovery = 0

bot = telebot.TeleBot("5224662237:AAHinmeM1NgsnRAqHIS1Vk55PzOgSwS0i_M")

def Starting_Сharacteristics():
    global hp, max_hp, dam, xp, gold, lvl, DamWeapon

    hp = 1000
    max_hp = 100
    dam = 1
    xp = 0
    gold = 10000
    lvl = 0
    DamWeapon = 0

def Indicators():
    global hp, max_hp, dam, DamWeapon, xp, lvl, gold

    Interface = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=False)
    YourHp = types.KeyboardButton("Здоровье: " + str(hp) + "/" + str(max_hp) + "❤")
    YourDam = types.KeyboardButton("Урон: " + str(dam + DamWeapon) + "🗡")
    YourXp = types.KeyboardButton("Опыт: " + str(xp) + "📚")
    YourLvl = types.KeyboardButton("Уровень: " + str(lvl) + "📖")
    YourGold = types.KeyboardButton("Золото: " + str(gold) +"🪙")
    Interface.add(YourHp, YourDam, YourGold, YourLvl, YourXp)

    return Interface

def Repeat ():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("💥Да!", callback_data="Repeat"))
    markup.add(types.InlineKeyboardButton("🖐Нет!", callback_data="NoRepeat"))

    return markup

def Travel(message):
    Interface = Indicators()

    bot.send_message(message.chat.id, "🌅 Выйдя за порог родного дома вы предвкушаете сладостный вкус предстоящих преключений!", reply_markup=Interface)
    bot.register_next_step_handler(message, event(message))

def spawn_monstr():
    probability = randint(1, 10)

    if probability >= 1 and probability <= 4:
        name_Spawn_monster = "Гоблин"
        return name_Spawn_monster
    if probability >= 5 and probability <= 7:
        name_Spawn_monster = "Орк"
        return name_Spawn_monster
    if probability == 8 or probability == 9:
        name_Spawn_monster = "Огр"
        return name_Spawn_monster
    if probability == 10:
        name_Spawn_monster = "Троль"
        return name_Spawn_monster

def Hp_SpawnMonstr(name_monster):
    global hp_monster

    if name_monster == "Гоблин":
        hp_monster = 30
        return hp_monster
    if name_monster == "Орк":
        hp_monster = 60
        return hp_monster
    if name_monster == "Огр":
        hp_monster = 85
        return hp_monster
    if name_monster == "Троль":
        hp_monster = 110
        return hp_monster

def Dam_SpawnMonstr(name_monster):

    if name_monster == "Гоблин":
        dam_monster = 15
        return dam_monster
    if name_monster == "Орк":
        dam_monster = 30
        return dam_monster
    if name_monster == "Огр":
        dam_monster = 45
        return dam_monster
    if name_monster == "Троль":
        dam_monster = 85
        return dam_monster

def priceGold(name):
    if name == "Гоблин":
        praice = 80
        return praice
    if name == "Орк":
        praice = 130
        return praice
    if name == "Огр":
        praice = 170
        return praice
    if name == "Троль":
        praice = 240
        return praice

def pricXpMonster(name):
    if name == "Гоблин":
        xpFromMonster = 25
        return xpFromMonster
    if name == "Орк":
        xpFromMonster = 50
        return xpFromMonster
    if name == "Огр":
        xpFromMonster = 75
        return xpFromMonster
    if name == "Троль":
        xpFromMonster = 100
        return xpFromMonster

def PresentationTheMonster (message):
    global name_monster, damage_monster, hp_monster

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🗡 Вступить в бой!", callback_data="Attack the monster!"))
    markup.add(types.InlineKeyboardButton("🏃Попытаться сбежать от монстра.",
                                          callback_data="Run away from the monster."))
    Presentation = "На вашему пути встал " + name_monster + ". Окинув взгядом его мускулатуру тела вы делаете вывод, что его здоровье ровно " + str(
        hp_monster) +  " единицам. Заметив грамосткое оружие в руках существа вы понимаете: он способен нанести " + str(
        damage_monster) + " урона за удар. Желаете с ним подраться?"
    bot.send_message(message.chat.id, text=Presentation, reply_markup=markup)

def levelUp(message):
    global xp, lvl

    if lvl <= 5 and xp >= 100:
        lvl += 1
        xp -= 100

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Максимальное здоровье на 15 едениц.", callback_data= "Increase maximum health"))
        markup.add(types.InlineKeyboardButton("Постоянный урон на 5 едениц.", callback_data="Increase permanent damage"))
        markup.add(types.InlineKeyboardButton("Полностью восстановить здоровье.", callback_data="Fully restore health"))
        NewLvl = "Вы перешли на новый уровень: " + str(lvl) +"!\n\n Вы можете увеличить:"
        bot.send_message(message.chat.id, text = NewLvl, reply_markup=markup)

    elif lvl <= 10 and xp >= 150:
        lvl += 1
        xp -= 150

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Максимальное здоровье на 15 едениц.", callback_data="Increase maximum health"))
        markup.add(
            types.InlineKeyboardButton("Постоянный урон на 5 едениц.", callback_data="Increase permanent damage"))
        markup.add(types.InlineKeyboardButton("Полностью восстановить здоровье.", callback_data="Fully restore health"))
        NewLvl = "Вы перешли на новый уровень: " + str(lvl) + "!\n\n Вы можете увеличить:"
        bot.send_message(message.chat.id, text = NewLvl, reply_markup=markup)

    elif lvl <= 15 and xp >= 200:
        lvl += 1
        xp -= 200

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Максимальное здоровье на 15 едениц.", callback_data="Increase maximum health"))
        markup.add(
            types.InlineKeyboardButton("Постоянный урон на 5 едениц.", callback_data="Increase permanent damage"))
        markup.add(types.InlineKeyboardButton("Полностью восстановить здоровье.", callback_data="Fully restore health"))
        NewLvl = "Вы перешли на новый уровень: " + str(lvl) + "!\n\n Вы можете увеличить:"
        bot.send_message(message.chat.id, text = NewLvl, reply_markup=markup)

    elif lvl <= 20 and xp >= 250:
        lvl += 1
        xp -= 250

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Максимальное здоровье на 15 едениц.", callback_data="Increase maximum health"))
        markup.add(
            types.InlineKeyboardButton("Постоянный урон на 5 едениц.", callback_data="Increase permanent damage"))
        markup.add(types.InlineKeyboardButton("Полностью восстановить здоровье.", callback_data="Fully restore health"))
        NewLvl = "Вы перешли на новый уровень: " + str(lvl) + "!\n\n Вы можете увеличить:"
        bot.send_message(message.chat.id, text = NewLvl, reply_markup=markup)

    elif lvl <= 20 and xp >= 300:
        lvl += 1
        xp -= 300

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Максимальное здоровье на 15 едениц.", callback_data="Increase maximum health"))
        markup.add(types.InlineKeyboardButton("Постоянный урон на 5 едениц.", callback_data="Increase permanent damage"))
        markup.add(types.InlineKeyboardButton("Полностью восстановить здоровье.", callback_data="Fully restore health"))
        NewLvl = "Вы перешли на новый уровень: " + str(lvl) + "!\n\n Вы можете увеличить:"
        bot.send_message(message.chat.id, text = NewLvl, reply_markup=markup)
    else:
        bot.register_next_step_handler(message, event(message))

def LevelUpMaxHp (message):
    global max_hp

    max_hp += 15
    Interface = Indicators()
    bot.send_message(message.chat.id, "Ваше максимальное здоровье увелечино и ровно:" + str(max_hp), reply_markup=Interface)
    bot.register_next_step_handler(message, event(message))

def LevelUpDam(message):
    global dam

    dam += 5
    Interface = Indicators()
    bot.send_message(message.chat.id, "Ваш постоянный урон увелечин на 5 едениц и равен:" + str(dam), reply_markup=Interface)
    bot.register_next_step_handler(message, event(message))

def LevelUpFullHp(message):
    global max_hp, hp

    hp -= hp
    hp += max_hp
    Interface = Indicators()
    bot.send_message(message.chat.id, "Ваше здоровье полностью восстановленно", reply_markup=Interface)
    bot.register_next_step_handler(message, event(message))

def ChoiceFaight (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🗡Атаковать монстра!", callback_data="Attack the monster!(On Fight"))
    markup.add(types.InlineKeyboardButton("🏃Попытаться сбежать от монстра.",
                                                      callback_data="Run away from the monster. (On Fight"))
    bot.send_message(message.chat.id, "Что будете делать?", reply_markup=markup)

def MovePlayer(message):
    global hp, dam, xp, gold, hp_monster, name_monster, price_Monstor, DamWeapon, priceXp_Monsotr

    if hp_monster > 0:
        hp_monster -= (dam + DamWeapon)
        if hp_monster <= 0:
            gold += price_Monstor
            xp += priceXp_Monsotr
            Interface = Indicators()
            KillTheMonster = "Вы нанесли монстру: " + str(dam + DamWeapon) + " урона. \n\n💀Вы убили монстра! Вы ясно понимаете: ваше мастерство ведения боя совершенствуется с каждым убитым врагом и ударом в бою. Сейчас количество твоего \
опыта ровно: " + str(xp)+  ". Чувство гордости за собственную состоятельность окутывает глаза непроглядной пеленой. Смакуя весь успех вы замечете – из \
только что убитого " + name_monster + "а таинственным образом высыпалась кучка монет в размере: " + str(price_Monstor) + " золотых"
            bot.send_message(message.chat.id, text=KillTheMonster, reply_markup=Interface)
            bot.register_next_step_handler(message, levelUp(message))
        elif hp_monster > 0:
            Remainder = "Вы нанесли монстру: " + str(dam + DamWeapon) + " урона. \n\n💚У монстра осталось: " + str(hp_monster) + " здоровья."
            bot.send_message(message.chat.id, text=Remainder)
            bot.register_next_step_handler(message, MoveMonster(message))

def MoveMonster (message):
    global hp, dam, DamWeapon, xp, lvl, max_hp, gold, name_monster, damage_monster

    hp -= damage_monster
    Interface = Indicators()

    MonsterDamage = "Ход монстра! \n\n⚒"+name_monster + " атакует вас и наносит " + str(damage_monster) + " урона"
    bot.send_message(message.chat.id, text=MonsterDamage, reply_markup=Interface)
    if hp > 0:
        bot.register_next_step_handler(message, ChoiceFaight(message))
    else:
        repeat = Repeat()
        end = name_monster + " оказался сильнее. Вы трагические погибли.\
                                     \nИгра окончена. \n\nЖелаете отправиться в новое приключение?"

        bot.send_message(message.chat.id, text=end, reply_markup=repeat)

def RunFight (message):
    global hp, damage_monster

    escapeAttempt = randint(1,2)

    if escapeAttempt == 1:
        markup = types.InlineKeyboardMarkup()
        markup.add()
        bot.send_message(message.chat.id, "Какой же он медленный и неуклюжый. Ваш побег прошёл успешно!")
        bot.register_next_step_handler(message, event(message))

    elif escapeAttempt == 2:
        hp -= damage_monster
        if hp > 0:
            NotRun = "Сбежать от монстра не получается. Из-за собсвтенной неуклюжести во время побега вы падаете,\
                                                                что позвляет монстру атакавать вас и нанести " + str(
                damage_monster) + " урона. \n\n🗡Прийдётся драться! \n\n😡В порыве ярости, резким рывком вы подрываете своё тело с земли и наотмашь бьёте врага!"
            Interface = Indicators()
            bot.send_message(message.chat.id, text=NotRun, reply_markup= Interface)
            bot.register_next_step_handler(message, MovePlayer(message))
        elif hp < 0:
            repeat = Repeat()
            Interface = Indicators()
            bot.send_message(message.chat.id, "Сбежать от монстра не получается. Из-за собсвтенной неуклюжести во время побега вы падаете,\
                                                            что позвляет монстру нанести фатальный удар по вам. В процессе битвы вы трагически погибаете.", reply_markup= Interface)
            bot.send_message(message.chat.id, "Желаете отправиться в приключение снова?", reply_markup=repeat)

def shop (message):
    global gold, hp, max_hp, DamWeapon, PrinterCostWeapon, PrinterDamWeapon

    weapon = ["Длинный меч", "Топор", "Кинжал", "Копьё"]
    weaponQuality = ["плохого качества", "среднего качества", "отличного качества"]

    Quality = choice(weaponQuality)
    NameSubject = choice(weapon)

    def DamWeapon_Q(Quality_Q, weapon_Q):
        global PrinterDamWeapon
        PrinterDamWeapon = 0

        if Quality_Q == "плохого качества":
            PrinterDamWeapon += 5
        elif Quality_Q == "среднего качества":
            PrinterDamWeapon += 10
        elif Quality_Q == "отличного качества":
            PrinterDamWeapon += 15

        if weapon_Q == "Длинный меч":
            PrinterDamWeapon += 40
        elif weapon_Q == "Топор":
            PrinterDamWeapon += 30
        elif weapon_Q == "Копьё":
            PrinterDamWeapon += 20
        elif weapon_Q == "Кинжал":
            PrinterDamWeapon += 10
        return PrinterDamWeapon

    def CostWeapon_Q(Quality_Q, weapon_Q):
        global PrinterCostWeapon
        PrinterCostWeapon = 0

        if Quality_Q == "плохого качества":
            PrinterCostWeapon += 100
        elif Quality_Q == "среднего качества":
            PrinterCostWeapon += 200
        elif Quality_Q == "отличного качества":
            PrinterCostWeapon += 300

        if weapon_Q == "Длинный меч":
            PrinterCostWeapon += 200
        elif weapon_Q == "Топор":
            PrinterCostWeapon += 150
        elif weapon_Q == "Копьё":
            PrinterCostWeapon += 100
        elif weapon_Q == "Кинжал":
            PrinterCostWeapon += 50

        return PrinterCostWeapon

    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton("💊Насыщенно красный элексир, который восстановит вам 30 здоровья.\
\nСтоимость элексира: 50 золота", callback_data="Elixir +30hp"))
    markup.add(types.InlineKeyboardButton("❣Большую банку наполненную богровой жидкостью, которая восстановит вам 100 здоровья.\
\nСтоимость элексира: 135 золота", callback_data="Elixir +100hp"))
    Selling_Weapons ="⚔"+ str(NameSubject) + " " + str(Quality) + " стоимостью " + str(CostWeapon_Q(Quality, NameSubject)) + " и уроном в " + str(DamWeapon_Q(Quality, NameSubject)) + " едениц."
    markup.add(types.InlineKeyboardButton(text=Selling_Weapons, callback_data="Selling_weapons"))
    markup.add(types.InlineKeyboardButton(text="✖На полках магазина нет интересующих вас товаров.", callback_data="ExitShop"))

    Store_Appearance = "Вы заходите в маленький приятный магазин. За прилавком стоит воодушевлённый вашим появлением торговиец ожидающий ваших действий.\
           \n\n🪙Резким движением запустив руку в карман ваших штанов вы слшыите звон. По глубине и плотности металического звона вы определяете ваше состояние в " + str(gold) + " золотых."
    bot.send_message(message.chat.id, text=Store_Appearance, reply_markup=markup)

def Buy (message):
    global gold, cost, recovery

    if gold >= cost:
        gold -= cost
        bot.register_next_step_handler(message, ExaminationMaxHp(message, recovery))
    else:
        bot.send_message(message.chat.id, "Для покупки этого предмета вам не хватает золота. Торговыец сразу подмечает данный и факт и обращает на вас тяжёлый, презренный взгялд в активном ождании вашего ухода.\
                                          \n\nВы поспешно покидаете магазин.")
        bot.register_next_step_handler(message, event(message))

Seller_Satisfied = "\n\n🗿Продавец довольный звонкой монетой быстро скрывается в дальней комнате магазина. Ясно одно: возвращаться к прилавку он не собирается. Вы покидаете магазин."

def ExaminationMaxHp (message, Replenishment):
    global hp, max_hp

    if hp+Replenishment > max_hp:
        hp -= hp
        hp += max_hp
        Interface = Indicators()

        bot.send_message(message.chat.id, "Ваше максимальное здоровье не может превысить значение в: " +str(max_hp) + ". Ваше здоровье восстановленно до предела!" + Seller_Satisfied, reply_markup=Interface)
        bot.register_next_step_handler(message, event(message))
    else:
        hp += Replenishment
        Interface = Indicators()
        bot.send_message(message.chat.id, "Вы чувствуете как элексир наполняет вас силой и заживляет старые раны." + str(hp) + Seller_Satisfied, reply_markup=Interface)
        bot.register_next_step_handler(message, event(message))

def Buy_Weapon (message):
    global DamWeapon, cost, gold, PrinterDamWeapon, dam, PrinterDamWeapon

    if gold >= cost:
        gold -= cost
        DamWeapon = PrinterDamWeapon
        Interface = Indicators()
        bot.send_message(message.chat.id, "\t  Благодаря новому оружие ваш урон увеличен и теперь равен: " + str(dam + DamWeapon) + " еденицам." + Seller_Satisfied, reply_markup=Interface)
        bot.register_next_step_handler(message, event(message))
    else:
        bot.send_message(message.chat.id, "Для покупки этого предмета вам не хватает золота. Торговыец сразу подмечает данный и факт и обращает на вас тяжёлый, презренный взгялд в активном ождании вашего ухода.\
                                          \n\nВы поспешно покидаете магазин.")
        bot.register_next_step_handler(message, event(message))

@bot.message_handler(commands=["start"])
def start(message):
    global hp, DamWeapon, gold, xp, lvl, dam, max_hp
    Starting_Сharacteristics()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🧭Отправиться в путешествие!", callback_data="Go on a trip!"))
    bot.send_message(message.chat.id, "Яркий свет солнечных лучей, купающий бледную кожу твоего лица бесцеремонно вырывает сознание из прекрасного, но уже забытого сна.\
Не торопясь встав с кровати и окинув взглядом маленькую, привычную комнату взор невольно падает на рабочий стол, расположенный в нескольких шагах от колыбели собственных мечтаний.\
Нагроможденный различными картами, пергаментами и книгами словно нарочно скидывает со своей поверхности лист с описанием далёких земель – земель отправиться к которым было давней мечтой.\
Прекрасная пора - не знание понятий: бедность, бегство, необходимость. \
\n\n🏞Сегодня ты твёрдо решаешь оборвать тонкую ленту собственной однообразной жизни и отправиться в путешествие. ",
                     reply_markup=markup)

def event(message):
    situation = randint(1, 3)

    if situation == 1:
        markup1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="🗺 Да!", callback_data="Yes, let's move on")
        key_no = types.InlineKeyboardButton(text="🛌 Нее. На сегодня хватит, нужно отдохнуть.",
                                            callback_data="No, we will stop.")
        markup1.add(key_yes, key_no)
        bot.send_message(message.chat.id, "Здесь нет ничего интересного. Продолжаем путь?", reply_markup=markup1)
    elif situation == 2:
        markup1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="💰 Да, зайду в магазин.", callback_data="Yes, go to the store")
        key_no = types.InlineKeyboardButton(text="🖼Нее, в этом нет необходимости.",
                                            callback_data="No, it's not necessary")
        markup1.add(key_yes, key_no)
        bot.send_message(message.chat.id, "🛖 Вы наткнулись на магазин. Хотите зайти?",
                         reply_markup=markup1)
    elif situation == 3:
        markup1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="🔎Проверю, что это такое",
                                             callback_data="I will not run from danger!")
        key_no = types.InlineKeyboardButton(text="😬Нет нужды рисковать, лучше обойти.",
                                            callback_data="No need to risk")
        markup1.add(key_yes, key_no)
        bot.send_message(message.chat.id, "❓Двигаясь на своём пути вы замечате активное движение в дали. Для избежания неприятных ситуаций принято решение: осесть в кустах и затаиться,\
в ожидании дальнейшего развития событий.", reply_markup=markup1)

@bot.callback_query_handler(func=lambda call: True)
def event_choice(call):
    global hp, max_hp, dam, xp, gold, hp_monster, DamWeapon, name_monster, price_Monstor, priceXp_Monsotr, damage_monster, cost, recovery, PrinterCostWeapon

    if call.data == "Yes, let's move on":
        bot.send_message(call.message.chat.id, "Продолжаем путешествие!")
        bot.register_next_step_handler(call.message, event(call.message))

    elif call.data == "Go on a trip!":
        bot.register_next_step_handler(call.message, Travel(call.message))

    elif call.data == "No, we will stop.":
        repeat = Repeat()
        bot.send_message(call.message.chat.id,"Из-за вашего желания оставаться на месте вы уснули. Пока вы спали на вас напал вампир и убил!\n\nЖелаете отправиться в приключение снова?", reply_markup=repeat)

    elif call.data == "Yes, go to the store":
        bot.register_next_step_handler(call.message, shop(call.message))

    elif call.data == "No, it's not necessary":
        bot.send_message(call.message.chat.id, "Продолжаем путешествие!")
        bot.register_next_step_handler(call.message, event(call.message))

    elif call.data == "Elixir +30hp":
        cost = 50
        recovery = 30
        bot.register_next_step_handler(call.message, Buy(call.message))

    elif call.data == "Elixir +100hp":
        cost = 135
        recovery = 100
        bot.register_next_step_handler(call.message, Buy(call.message))

    elif call.data == "Selling_weapons":
        cost = PrinterCostWeapon
        bot.register_next_step_handler(call.message, Buy_Weapon(call.message))

    elif call.data == "ExitShop":
        bot.send_message(call.message.chat.id, "Поняв, что вы не србираетесь оставлть деньги в магазине торговец начинает презительно смотреть на вас. Вы покидаете магазин.")
        bot.register_next_step_handler(call.message, event(call.message))

    elif call.data == "No need to risk":
        retreat = randint(1, 2)
        if retreat == 1:
            name_monster = spawn_monstr()
            hp_monster = Hp_SpawnMonstr(name_monster)
            damage_monster = Dam_SpawnMonstr(name_monster)
            price_Monstor = priceGold(name_monster)
            priceXp_Monsotr = pricXpMonster(name_monster)
            bot.send_message(call.message.chat.id,
                             "Слишком поздно! Неясная фигура с большой скоростью направляется в вашу сторону.")
            bot.register_next_step_handler(call.message, PresentationTheMonster(call.message))
        elif retreat == 2:
            bot.send_message(call.message.chat.id,
                             "По мере пребывания в зарослях неизвестный объект впереди удалялся, а сейчас и вовсе скрылся из виду. Путь свободен!")
            bot.register_next_step_handler(call.message, event(call.message))

    elif call.data == "I will not run from danger!":
        name_monster = spawn_monstr()
        hp_monster = Hp_SpawnMonstr(name_monster)
        damage_monster = Dam_SpawnMonstr(name_monster)
        price_Monstor = priceGold(name_monster)
        priceXp_Monsotr = pricXpMonster(name_monster)
        bot.send_message(call.message.chat.id, "Отправляемся")
        bot.register_next_step_handler(call.message, PresentationTheMonster(call.message))

    elif call.data == "Attack the monster!":
        bot.register_next_step_handler(call.message, ChoiceFaight(call.message))

    elif call.data == "Run away from the monster.":
        bot.register_next_step_handler(call.message, RunFight(call.message))

    elif call.data == "Attack the monster!(On Fight":
        bot.register_next_step_handler(call.message, MovePlayer(call.message))

    elif call.data == "Run away from the monster. (On Fight":
        bot.register_next_step_handler(call.message, RunFight(call.message))

    elif call.data == "Increase maximum health":
        bot.register_next_step_handler(call.message, LevelUpMaxHp(call.message))

    elif call.data == "Increase permanent damage":
        bot.register_next_step_handler(call.message, LevelUpDam(call.message))

    elif call.data == "Fully restore health":
        bot.register_next_step_handler(call.message, LevelUpFullHp(call.message))

    elif call.data == "Repeat":
        bot.register_next_step_handler(call.message, start(call.message))

bot.polling(none_stop=True)
