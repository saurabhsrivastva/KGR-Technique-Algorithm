def algo(all_in_one_title, Search_Volume, Difficulty):

    KGR= float(all_in_one_title)/float(Search_Volume)
    
    print(KGR)
    if KGR<0.25 and Difficulty<10:
       print("You Should definately write on this keyword")
    elif 0.25<KGR<1.0 and Difficulty<20 or 0.25<KGR<1.0 and 10<Difficulty<20:
       print("Comparitively difficult but still considerable")
    else:
       print("Definately not suitable for new blogs")


algo(float(input("Enter all in one title")), 
float(input("Enter Keyword Volume")), 
float(input("Enter Search Difficulty")))        
