from telebot import TeleBot
from telebot import types
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup
from telebot.types import KeyboardButton , ReplyKeyboardMarkup
from config import channel, TOKEN
import time


mychatid = 963475140
bot = TeleBot(token=TOKEN)



"""
 UID = message.from_user.username
 UFN = message.from_user.firstname
"""



"""
if message.text == "لغو ❌":
    cncltct(message)
elif message.text == "شروع مجدد":
    start(message)
else:
"""





inbutton1 = InlineKeyboardButton(text="🔹چنل اول ما🔹", url="https://t.me/russie_tuday2024")
inbutton2 = InlineKeyboardButton(text="🔹چنل دوم ما🔹", url="https://t.me/havashi_russ_2022")
inbutton3 = InlineKeyboardButton(text="🔹چنل آگهی ما🔹", url="https://t.me/niazmndiha_2024_rus")
inbutton4 = InlineKeyboardButton(text="🔹بررسی عضویت🔹", callback_data="join")
markup1 = InlineKeyboardMarkup(row_width=1)
markup1.add(inbutton1, inbutton2 , inbutton3 , inbutton4)
markchnnl = InlineKeyboardMarkup(row_width=1)
markchnnl.add(inbutton1 , inbutton2 , inbutton3)

# options
button1 = KeyboardButton(text="ثبت آگهی 📮")
button2 = KeyboardButton(text="قوانین 📌")
button3 = KeyboardButton(text="پشتیبانی ⚠️")
button4 = KeyboardButton(text="کانال ها 📣")
button5 = KeyboardButton(text="آگهی های من 👀")
markup2 = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markup2.row(button1)
markup2.row(button2 , button3)
markup2.row(button4)



# pending

# options - button7
inbutton17 = InlineKeyboardButton(text="آگهی های درحال تایید من📌" , callback_data="pending")
inbutton18 = InlineKeyboardButton(text="آگهی های فعال من✅" , callback_data="active")
inbutton19 = InlineKeyboardButton(text="آگهی های منقضی شده من❌" , callback_data="cancled")
markup5 = InlineKeyboardMarkup(row_width=1)
markup5.add(inbutton17 , inbutton18 , inbutton19)


 #daste

inbutton6 = types.KeyboardButton(text="اجاره تخت" )
inbutton7 = types.KeyboardButton(text="اجاره اتاق" )
inbutton8 = types.KeyboardButton(text="اجاره خانه" ,)
inbutton9 = types.KeyboardButton(text="متقاضی تخت")
inbutton10 = types.KeyboardButton(text="متقاضی اتاق")
inbutton11 = types.KeyboardButton(text="متقاضی خانه",)
inbutton12 = types.KeyboardButton(text="نیازمندی ها" )
inbutton13 = types.KeyboardButton(text="خرید کالا" )
inbutton14 = types.KeyboardButton(text="فروش کالا")
inbutton15 = types.KeyboardButton(text="خرید بار")
inbutton16 = types.KeyboardButton(text="فروش بار")
inbutton17 = types.KeyboardButton(text="خرید روبل" )
inbutton18 = types.KeyboardButton(text="فروش روبل")
inbutton19 = types.KeyboardButton(text="خرید ارز دیجیتال",)
inbutton20 = types.KeyboardButton(text="فروش ارز دیجیتال" )
#inbutton21 = types.KeyboardButton(text="خدمات" )
inbuttoncn = KeyboardButton(text="لغو ❌" )
markupdaste = ReplyKeyboardMarkup(resize_keyboard=True)
markupdaste.row(inbutton6, inbutton7, inbutton8)
markupdaste.row(inbutton9, inbutton10, inbutton11)
markupdaste.row(inbutton12, inbutton13, inbutton14)
markupdaste.row(inbutton15, inbutton16)
markupdaste.row(inbutton17, inbutton18)
markupdaste.row(inbutton19, inbutton20)
#markupdaste.row(inbutton21)
markupdaste.row(inbuttoncn)


buttoncn = KeyboardButton(text="لغو ❌")
buttoncnmarkup = ReplyKeyboardMarkup(resize_keyboard=True)
buttoncnmarkup.add(buttoncn)


 #gharardad
inbuttongharardad1 = KeyboardButton(text="کوتاه مدت" )
inbuttongharardad2 = KeyboardButton(text="بلند مدت" )
inbuttongharardad3 = KeyboardButton(text="بدون قرارداد" )
markupgharardad = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markupgharardad.add(inbuttongharardad1 , inbuttongharardad2 , inbuttongharardad3)

buttonprice = KeyboardButton(text="ماهانه")
buttonprice2 = KeyboardButton(text="روزانه")
markupprice = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
markupprice.add(buttonprice , buttonprice2)

buttontavafogh = KeyboardButton(text="توافقی")
marktavafogh = ReplyKeyboardMarkup(row_width=1 , resize_keyboard=True)
marktavafogh.add(buttontavafogh , buttoncn)

buttonacept = KeyboardButton(text="تایید آگهی")
buttonreject = KeyboardButton(text="لغو آگهی")
accorejmarkup = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
accorejmarkup.add(buttonacept , buttonreject)

irtoit = KeyboardButton(text="ایران به روسیه")
ittoir = KeyboardButton(text="روسیه به ایران")
country = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
country.add(irtoit , ittoir , buttoncn)


inbutton24 = KeyboardButton(text="مسکو")
inbutton25 = KeyboardButton(text="نووسیبیرسک" )
inbutton26 = KeyboardButton(text="سن_پترزبورک" )
inbutton27 = KeyboardButton(text="نیژنووگراد")
inbutton28 = KeyboardButton(text="کازان")
inbutton29 = KeyboardButton(text="اولیانوفسک")
inbutton30 = KeyboardButton(text="سامارا")
inbutton31 = KeyboardButton(text="روستوف")
inbutton32 = KeyboardButton(text="اومسک")
inbutton33 = KeyboardButton(text="اوفا")
inbutton34 = KeyboardButton(text="ولگوگراد")
inbutton35 = KeyboardButton(text="پرم")
inbutton36 = KeyboardButton(text="ورونژ")
inbutton37 = KeyboardButton(text="ولادی_وستوک")
inbutton38 = KeyboardButton(text="سایر")
inbuttoncn = KeyboardButton(text="لغو ❌")
markupcity = ReplyKeyboardMarkup(row_width=3)
markupcity.add(inbutton24, inbutton25, inbutton26, inbutton27, inbutton28, inbutton29, inbutton30, inbutton31, inbutton32, inbutton33,inbutton34, inbutton35)
markupcity.row(inbutton36, inbutton37)
markupcity.add(inbutton38)
markupcity.row(inbuttoncn)


irancity1 = KeyboardButton(text="تهران")
irancity2 = KeyboardButton(text="مشهد")
irancity3 = KeyboardButton(text="اصفهان")
irancity4 = KeyboardButton(text="تبریز")
irancity5 = KeyboardButton(text="شیراز")
irancity6 = KeyboardButton(text="کرج")
irancity7 = KeyboardButton(text="کرمانشاه")
irancity8 = KeyboardButton(text="اهواز")
irancity9 = KeyboardButton(text="قم")
irancity10 = KeyboardButton(text="زاهدان")
irancity11 = KeyboardButton(text="رشت")
irancity12 = KeyboardButton(text="ارومیه")
irancity13 = KeyboardButton(text="یزد")
irancity14 = KeyboardButton(text="کرمان")
irancity15 = KeyboardButton(text="همدان")
irancity16 = KeyboardButton(text="اراک")
irancity17 = KeyboardButton(text="بندرعباس")
irancity18 = KeyboardButton(text="اردبیل")
irancity19 = KeyboardButton(text="قزوین")
irancity20 = KeyboardButton(text="سنندج")
irancity21 = KeyboardButton(text="زنجان")
irancity22 = KeyboardButton(text="ساری")
irancity23 = KeyboardButton(text="گرگان")
irancity24 = KeyboardButton(text="سایر")
irancitymarkup = ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
irancitymarkup.add(irancity1 , irancity2 , irancity3 , irancity4 , irancity5 , irancity6 , irancity7 , irancity8 , irancity9 , irancity10 , irancity11 , irancity12 , irancity13 , irancity14 , irancity15 , irancity16 , irancity17 , irancity18 , irancity19 , irancity20)
irancitymarkup.row(irancity21 , irancity22 , irancity23)
irancitymarkup.row(irancity24)

foreuro2 = KeyboardButton(text="انتخاب روش ها")
foreuro2mark = ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
foreuro2mark.add(foreuro2 , buttoncn)

paymethod1 = KeyboardButton(text="PayPal")
paymethod2 = KeyboardButton(text="ارز دیجیتال")
paymethod3 = KeyboardButton(text="Monse")
paymethod4 = KeyboardButton(text="IBAN")
paymethod5 = KeyboardButton(text="نقدی حضوری")
paymethod6 = KeyboardButton(text="سایر")
paymethod = ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
paymethod.add(paymethod1 , paymethod2 , paymethod3)
paymethod.row(paymethod4, paymethod5)
paymethod.row(paymethod6)


paymethodtwo = ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
paymethodtwo.add(paymethod1 , paymethod2 , paymethod3)
paymethodtwo.row(paymethod4, paymethod5)



notozih  = KeyboardButton(text="بدون توضیحات")
tozihmark = ReplyKeyboardMarkup(row_width=1)
tozihmark.add(notozih , buttoncn )



startagain = KeyboardButton(text="شروع مجدد")
main = ReplyKeyboardMarkup (row_width=1)
main.add(startagain , buttoncn)

main2 = ReplyKeyboardMarkup (row_width=1)
main2.add(buttontavafogh,startagain , buttoncn)

tron = KeyboardButton(text="ترون , TRON")
theter = KeyboardButton(text="تتر , USDT")
btcm = ReplyKeyboardMarkup(row_width=1)
btcm.add(tron , theter)

withoutax = KeyboardButton(text="بدون عکس")
axmark = ReplyKeyboardMarkup(row_width=1)
axmark.add(withoutax , buttoncn)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text="""
        ♾️ کاربر عزیز ! سلام👋. به ربات نیازمندی های Rus bazar خوش آمدید. 🤩

✅ توجه داشته باشید که آگهی های شما پس از تایید در کانال روس بازار منتشر خواهد شد. لطفا با معرفی روس بازار به دوستان خود از این فعالیت حمایت کنید.

🔴 تایید صحت آگهی ها و درخواست های ثبت شده در روس بازار به عهده کاربران عزیز میباشد و Rus bazar هیچگونه مسئولیتی را در قبال آگهی ها نمی پذیرد.

🌐 خدمت رسانی به هم وطنان و هم زبانان عزیز از افتخارات ماست.


❌این ربات توسط گروه راشسان (Rush sun) توسعه یافته است!❌


        """, reply_markup=markup1)








