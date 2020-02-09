####################################################################################################
#author: Arjun Parajuli
#Date: 2/8/2020

#Collaborators:
    #Avinas Aryal
    #Nabin Shrestha
    #Sushant Gupta

####################################################################################################

#This is the simple program that will calculate the total expense of any group and split
#it among the members.


#Pros: Program is a simple calculator which will help to split the expenses within the group
#      Program will handle some of the exceptions on data type.


#Cons: The program is limited to execute only on execution terminal, OOP and GUI can be implemented.
#      on providing the same data (person's name) twice the data will be overwritten.



#input to get the member name
name=input(u"Name of the person:  ")
#initialization of number of group members
numOfPerson=0
#initialization of dictionary to assign the detail according with the person 
myStrDict=dict()

#while loop to add the group members untill user says "DONE"
while name.upper()!="DONE":
    
        #increment of number of person in the group
        #as it starts to iterate over while loop
        numOfPerson+=1
        #initialization of the string 
        myStr=str()
        #initialization of personal total expense
        personalTot=0
        #prompt to user to input the place the member bought the stuff from
        amtStr=input(u"Place where he brought the stuff or type 'NO': ")

        #while loop to input all the details of the expense done by one person
        while amtStr.upper()!="NO":
            amt= input(u"How much ($)? : ")
            #exception handeling if user enters non-integer value
            while not amt.isdigit() and amt.isalnum():
                print("Invalid Entry")
                amt= input(u" Please enter the amount ($)")
            #implement if same member exit in the dictionary


            #adding personal expense
            personalTot+=float(amt)
            #concatination of the person's expense with where he brought the stuff from
            amtWithStr = "{0:20s}${1:4.2f}".format(amtStr,float(amt))
            myStr+=amtWithStr+"\n"
            #prompt to user to input another place if s/he has spend in any other place 
            amtStr=input(u"Any other places he brought the suff from ?(if Not type NO): ")

        #concatinating total expense of the person with the detail of the expense
        #to create the string
        myStr+=("="*40)+"\n"+"{0:20s}${1:4.2f}".format("Total",float(personalTot))+"\n"+("="*40)+"\n"
        #assigning the personal toatal expense and expense detail string
        #with person using dictionary
        myStrDict[name]=[myStr,personalTot]
        name = input(u"Any other person? Please enter the name here (or type DONE):  ")


#selection for the case if user doesn't give any input
if len(myStrDict)!=0:
    #initialization of grand total expense
    gTot=0


    #loop to print the name of the member and his/her personal expense
    #and to calculate the total expense of the group
    for nameKey in myStrDict:
        print(nameKey,"\n",myStrDict[nameKey][0])
        gTot+=myStrDict[nameKey][1]


    #printing total expense
    print("="*40)
    print("Grand Total",gTot)
    print("="*40)

    #loop to go through the dictionary and to calculate the personal
    #remaining balance within the group
    for nameKey in myStrDict:
        #calulation of personal remaining balance 
        personalRemainingAmount=myStrDict[nameKey][1]-(gTot/len(myStrDict))

        #using selection to give the final masssage about the calculation
        if personalRemainingAmount<0:
            print(nameKey,"will have to pay $",abs(personalRemainingAmount))
        elif personalRemainingAmount>0:
            print(nameKey,"will collect $",personalRemainingAmount)
        else:
            print(nameKey,"is settled.")
#else condition 
else:
    print("No entry, No calculation can be done!")



