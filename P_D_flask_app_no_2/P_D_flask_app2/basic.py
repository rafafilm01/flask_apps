# example of template forms 
# example of a custom made 404 page not found 
#request library used for getting the information from the form 
#NOTE ! make sure to use the correct bootstrap version as script links will work differently , current bootstrap for the project 4.6
#username validation test under username_check.html . Make sure username provided by the user meets our conditions 

from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/sign_up')
def sign_up_form():
    return render_template('signUp.html')

@app.route('/thank_you')
def thank_you ():
    #extracting the variables form the HTML form 
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankYou.html', first=first, last=last)    

#custom mode 404 page for any other traffic that is not described in other views , e stands for error , 404 describes incorrect get request
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#PART 1 page to create a username and carry out basic validation (1 upper case , 1 lower case and 1 number)
@app.route('/username')
def new_username():
    return render_template('username_check.html')

#PART 2return page with username name and validation checks
# in real life scenario failure to provide username that is not strong enough would redirect the user o a different page (or refresh the form with an additional message)
@app.route('/username_validation')
def username_validation():
    username= request.args.get('username')
    
    #working out the password strength 
    # if username.isnumeric()==True and username.isupper()==True and username.islower()==True:
    #     print ('password criteria met ')
    # else:
    #     if username.isnumeric()== False:
    #         print('please provide at least 1 number')
    #     if username.islower() ==False:
    #         print('please provide at least 1 lower case letter')
    #     if username.isupper()== False:
    #         print('please provide at least 1 upper case letter ')    
    
    #working out password strength TAKE 2 , creating a list and counting the number of uppercase /lowerace / numbers . If at the end of the list (string) the count is 0 it means that there are no characters of this type in the username 
    upper_case_char =0
    lower_case_char=0
    number_chars =0
    for i in list(username):
        if i.isupper():
            upper_case_char +=1
        elif i.islower():
            lower_case_char+=1
        elif i.isnumeric():
            number_chars+=1
            
    print(f'lower case count:  {upper_case_char}')   
    print(f'lower case count: {lower_case_char}')
    print(f'number count: {number_chars}')     
   
    #TAKE 3 using dict comprehension to check if conditions are met and them passing the result to username_verification.html . All the logic is handled in basic.py
    #to start off , boolena flags are set to FALSE and only will be changed if dict comprehen. changes them 
    # lower_letter=False
    # upper_letter=False
    # digit_char=False
    # lower_letter = any(i.islower() for i in username)
    # upper_letter = any(i.isupper() for i in username)
    # digit_char = any(i.isdigit() for i in username)
    
    # report = lower_letter and upper_letter and digit_char
    #these dict comprehensions will bring out boolean statements 
    return render_template('username_verification.html', username=username, upper_case_char=upper_case_char, lower_case_char=lower_case_char, number_chars=number_chars )

#return render for TAKE 3
    #return render_template('username_verification.html', username=username,report=report, lower_letter=lower_letter, upper_letter=upper_letter, digit_char=digit_char)

if __name__ =='__main__':
    app.run(debug=True)
