

# . CHARACTER & VARIABLE DEFINITIONS ---
define g = Character("Ganji Chudail")
define b = Character("Birju")
define r = Character("Kapali Chudail")

#  Variables 
default anger_points = 0
default betrayal_points = 0
default respect_points = 0

#audio
define audio_shout = "audio/shout.mp3"
# --- 3. SPRITE DEFINITIONS ---
image ganji_happy = "images/ganji_happy.png"
image ganji_normal = "images/ganji_normal.png" 
image ganji_sad = "images/ganji_sad.png"
image ganji_angry = "images/ganji_angry.png"

image birju_idle = "images/birju_idle.png"
image birju_shocked = "images/birju_shocked.png"

image kapali_shocked = "images/kapali_shocked.png"
image kapali_happy = "images/kapali_happy.png"
image kapali_angry = "images/kapali_angry.png"

# --- 4. BACKGROUNDS ---
image bg_kitchen = "images/kitchen.jpg"
image bg_park = "images/park.jpg"

label start:
    

    # --- CYCLE 1: THE MORNING INSULT ---
    scene bg_kitchen:
        zoom 1.5
    show ganji_happy at truecenter:
        zoom 2.0 
    g "Good morning Birju! Aaj dekho, maine naya face wash use kiya hai."
    
    hide ganji_happy
    show birju_idle at truecenter:
        zoom 2.0
    b "Good morning Ganji ji... Face wash toh theek hai, par aaj aapka wazan thoda zyada lag raha hai."
    b "Kya aapne raat ko chupke se 10 parathe khaye hain?"
    
    hide birju_idle
    show ganji_sad at truecenter:
        zoom 2.0
    "ganji is sad!"
    g "Birju! Tum hamesha subah-subah meri beizzati karte ho. Kya main sach mein moti hoon?"
    menu:
        "SHUT HIM UP":
        
            $ anger_points += 10
            g "Zabaan sambhal kar Birju! Tum khud ek chalti-phirti bhains lagte ho!"
            hide ganji_sad
            show birju_shocked at truecenter:
                zoom 2.0
            b "Arre... main toh bas mazaak kar raha tha!"
            hide birju_shocked
        "CRY AND AGREE":
            $ respect_points += 5
            g "Haan... shayad tum sahi keh rahe ho. Mujhe exercise ki zaroorat hai."
    hide ganji_sad
    show ganji_happy at truecenter:
        zoom 2.0
    g "Main park ja rahi hoon paseena bahane. Khana paka kar rakhna!"
    hide ganji_happy
    
    show birju_idle at truecenter:
        zoom 2.0 
    b "Jao jao... ab yahan meri asli rani aayegi!"
    hide birju_idle

    # --- CYCLE 2: THE PARK CARDIO ---
    scene bg_park with fade:
        zoom 1.5
    show ganji_sad at truecenter:
        zoom 2.0
    g "Uff! Kitni garmi hai. Thodi der rest karke ek dance reel banati hoon."
    g "Hey Bhagwan! Mera phone toh main kitchen ke shelf pe hi bhool gayi!"
    g "Ab poora rasta wapas jana padega... cardio toh raste mein hi ho gaya mera."
    
    hide ganji_sad
    scene bg_kitchen with fade:
        zoom 1.5

    # --- CYCLE 3: THE KITCHEN BETRAYAL ---
    show kapali_happy at truecenter:
        zoom 2.0
    r "Raja ji, Ganji toh gayi park mein. Ab hum maze karenge!"
    r "Uska sar toh mirror jaisa chamakta hai, par mere silky baal toh dekho."
    
    hide kapali_happy
    show birju_idle at truecenter:
        zoom 2.0
    b "Haan meri rani! Ganji ke paas sirf diet plan hai, tumhare paas toh mera dil hai."
    
    hide birju_idle

    "KNOCK KNOCK!"
    "BIRJU! DARWAZA KHOLO!"

    menu:
        "SCREAM OUTSIDE":
            show ganji_angry at truecenter:
                zoom 2.0
            g "BIRJU! Agar darwaza nahi khola toh main ise magic se tod dungi!"
            hide ganji_angry
        "ACT POLITE":
            show ganji_normal at truecenter:
                zoom 2.0
            g "Birju, mera phone reh gaya hai. Please darwaza kholo."
            hide ganji_normal

    # --- CYCLE 4: THE CONFRONTATION ---
    with hpunch 
    show ganji_normal at truecenter:
        zoom 2.0
    g "Kapali?! Tu meri sagee behen hokar yahan mere pati ke saath kya kar rahi hai?"
    
    hide ganji_normal
    show kapali_happy at truecenter:
        zoom 2.0
    r "Didi! Aap itni jaldi? Hum toh bas... biryani ki recipe discuss kar rahe the."
    
    hide kapali_happy
    show birju_shocked at truecenter:
        zoom 2.0
    b "Nahi Kapali! Ab bohot hua. Ganji, main aur Kapali ab saath rahenge. Tum jao exercise karo!"

    menu:
        "FIGHT KAPALI":
            $ betrayal_points += 20
            g "Kapali! Maine tujhe bachpan mein apne purane toys diye, aur aaj tu mera pati chura rahi hai?"
        "SCOLD BIRJU":
            $ anger_points += 20
            g "Birju! Maine tere liye pichle hafte makkhan wala paratha choda, aur ye tera sila hai?"

    # --- CYCLE 5: THE SISTER ROAST ---
    hide birju_shocked
    show kapali_angry at truecenter:
        zoom 2.0
    r "Didi! Toys purane ho gaye! Birju ko ab silky baal chahiye, aapka mirror wala sar nahi!"
    r "Aap reel banati raho, main Birju ke liye asli biryani banati hoon."
    
    hide kapali_angry
    show birju_idle at truecenter:
        zoom 2.0
    b "Haan! Kapali roz dher saare parathe khilati hai, tum toh bas calories count karti ho!"

    menu:
        "EXPOSE THE WIG":
            g "Birju! Ye tumhara ullu bana rahi hai. Iske ye silky baal nakli hain, ye wig hai!"
            hide birju_idle
            show kapali_shocked at truecenter:
                zoom 2.0
            r "Nahi! Ye asli hain! Maine kal hi inme dher sara tel lagaya hai!"
            hide kapali_shocked
        "EXPOSE THE DEBT":
            g "Kapali! Birju ke paas ek rupaya nahi hai. Iska poora kharcha mere card se chalta hai!"
            hide birju_idle
            show birju_shocked at truecenter:
                zoom 2.0
            b "Ganji! Itni zor se sach mat bolo, meri image kharab ho jayegi!"
            hide birju_shocked

    # --- CYCLE 6: THE VACATION DRAMA ---
    show birju_idle at truecenter:
        zoom 2.0
    b "Chalo Kapali, hum yahan se nikalte hain. Hum Singapore jayenge ghoomne!"
    b "ESLEY DIVORCE KARKEY SAB PAISA UDAHENGEY"
    
    hide birju_idle
    show ganji_angry at truecenter:
        zoom 2.0
    g "Singapore? Mere bank account se paise chori karke jaoge? "
    g "paisa milega toh gaogey"

    menu:
        "BLOCK THE EXIT":
            g "Jab tak mera phone aur card wapas nahi milta, koi bahar nahi jayega!"
        "CALL NEIGHBORS":
            g "Padosiyo! Dekho ye chorni meri behen mera ghar aur pati loot rahi hai!"

    # --- CYCLE 7: THE FINAL STAND ---
    hide ganji_angry
    show kapali_happy at truecenter:
        zoom 2.0
    r "Didi, ab aap akeli raho aur exercise karo. Hum toh chale maze karne!"
    r "birju ko apka aanda jasa sar nahi pasand hai"
    hide kapali_happy
    show ganji_angry at truecenter:
        zoom 3.0
    g "MEYNEY TOH EY SAB GHARBAR MUMMY KEY NAAM PAYE RAKHA HEEN"
    g "HAHAHHAAHHAHAHHHAHHAHAA"    
    g "BOHOT HO GAYA! AB GANJI CHUDAIL KA ASLI GUSSA DEKHO!"
    hide ganji_angry
    show birju_shocked:
          zoom 2.0
    b "maf karo babbyyy!! hum tumsey hi toh pyaar karte heen "
    b "apka sar hamara fav hai"
    hide birju_shocked
    show ganji_angry at truecenter:
        zoom 3.0    
    menu:
        "KICK THEM OUT":
            g "ja rey jozu tumey aacha wo chai wala hai"
            g "hum  usisey shaadi karengyi"
            "WON"
            $ game_ending = "VICTORY"
        "FORGIVE HIM":
            g "thik hey baby maf kiya!"
            "LOST"
            $ game_ending = "DANCE_QUEEN"

return 