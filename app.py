# ===========
#   Imports
# ===========
from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy
import sqlite3 as sql
from flask_cors import CORS, cross_origin
# ===================
#   Flask instance
# ===================
app = Flask(__name__)

# ======================
#   Allow Cross Origin
# ======================
@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
    
# ==================================
#  Insert message in Database(Contact Us)
# ==================================
def insertMessage(Name,Email,Message):
    con = sql.connect("test.db")
    cur = con.cursor()
    query = ("""INSERT INTO MESSAGE
             (Name,Email,Message)
             VALUES ('%s','%s','%s')""" %
             (Name,Email,Message))
    cur.execute(query)
    con.commit()
    con.close()

# ==================================
#  Insert data in database (SIGNUP)
# ==================================
def insertUser(FIRSTNAME,LASTNAME,USERNAME, PASSWORD, CITY,STATE,PINCODE):
    con = sql.connect("test.db")
    cur = con.cursor()
    pincode=int(PINCODE)
    query = ("""INSERT INTO NEW
             (FIRSTNAME,LASTNAME,USERNAME, PASSWORD, CITY,STATE,PINCODE)
             VALUES ('%s','%s','%s','%s','%s','%s',%d)""" %
             (FIRSTNAME,LASTNAME,USERNAME, PASSWORD, CITY,STATE,pincode))
    cur.execute(query)
    con.commit()
    con.close()


# =====================================
#  Validating data in database (LOGIN)
# =====================================
def validUser(USERNAME, PASSWORD):
    con = sql.connect("test.db")
    cur = con.cursor()
    query = ("""SELECT * FROM NEW
             where USERNAME = '%s' and PASSWORD = '%s'
             """ %
             (USERNAME, PASSWORD))
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    return data



#app = Flask(__name__, template_folder='./templates', static_folder='./static')

# =====================================
#  Routing
# =====================================
@app.route('/')

def hello_world():

    return render_template('Home_Main.html')
    
    
@app.route('/message', methods=['POST','GET'])

def mess():

    if request.method=='POST':
     Name = request.form['Name']
     Email = request.form['Email']
     Message = request.form['Message']
     insertMessage(Name,Email,Message)
     return "Message Sent"
    else:
        return "Unsuccesful"

@app.route('/geoLoc', methods=['POST','GET'])

def Location():
 
    
    return render_template('city2.html')

# =====================================
#  SignIn
# =====================================
@app.route('/signin/', methods=['POST','GET'])

def signin():
    if request.method == 'POST':
        rd = validUser(request.form['USERNAME'], request.form['PASSWORD'])
        if rd:
            return render_template('city2.html')
        else:
            return "UnSucessful login"
    else:
        return render_template('Login.html')

# =====================================
#  SignUp
# =====================================

@app.route('/signup/', methods=['POST','GET'])

def signup():
    if request.method == 'POST':
        FIRSTNAME = request.form['FIRSTNAME']
        LASTNAME = request.form['LASTNAME']
        USERNAME = request.form['USERNAME']
        PASSWORD = request.form['PASSWORD']
        CITY = request.form['CITY']
        STATE = request.form['STATE']
        PINCODE = request.form['PINCODE']
        insertUser(FIRSTNAME,LASTNAME,USERNAME, PASSWORD, CITY,STATE,PINCODE)
        return redirect(url_for('signin'))
    else:
        return render_template('Index1.html')


# =====================================
#  Pune Data
# =====================================

@app.route('/loadMap1', methods=['POST','GET'])

def Pune():
    return render_template('Punestreet.html')
    
@app.route('/PMap1', methods=['POST','GET'])
def PuneMap1():    
    return render_template('Pune_Maps/Aapte road.html')

@app.route('/PMap2', methods=['POST','GET'])
def PuneMap2():    
    return render_template('Pune_Maps/Ashok Kamathe Path.html')    

@app.route('/PMap3', methods=['POST','GET'])
def PuneMap3():    
    return render_template('Pune_Maps/Anudh.html')

@app.route('/PMap4', methods=['POST','GET'])
def PuneMap4():    
    return render_template('Pune_Maps/Baner.html')

@app.route('/PMap5', methods=['POST','GET'])
def PuneMap5():    
    return render_template('Pune_Maps/Budhwa Peth.html')

@app.route('/PMap6', methods=['POST','GET'])
def PuneMap6():    
    return render_template('Pune_Maps/Fatima Nagar.html')

@app.route('/PMap7', methods=['POST','GET'])
def PuneMap7():    
    return render_template('Pune_Maps/Fountain Road.html')

@app.route('/PMap8', methods=['POST','GET'])
def PuneMap8():    
    return render_template('Pune_Maps/Koregaon Park.html')

@app.route('/PMap9', methods=['POST','GET'])
def PuneMap9():    
    return render_template('Pune_Maps/Kothrud.html')

@app.route('/PMap10', methods=['POST','GET'])
def PuneMap10():    
    return render_template('Pune_Maps/Kulkarni Peth.html')

@app.route('/PMap11', methods=['POST','GET'])
def PuneMap11():    
    return render_template('Pune_Maps/Magarpatta.html')

@app.route('/PMap12', methods=['POST','GET'])
def PuneMap12():    
    return render_template('Pune_Maps/Marido Colony.html')

@app.route('/PMap13', methods=['POST','GET'])
def PuneMap13():    
    return render_template('Pune_Maps/Marketyard.html') 

@app.route('/PMap14', methods=['POST','GET'])
def PuneMap14():    
    return render_template('Pune_Maps/National Society.html') 

@app.route('/PMap15', methods=['POST','GET'])
def PuneMap15():    
    return render_template('Pune_Maps/New Nana Peth.html') 

@app.route('/PMap16', methods=['POST','GET'])
def PuneMap16():    
    return render_template('Pune_Maps/Old Wadarwadi.html') 

@app.route('/PMap17', methods=['POST','GET'])
def PuneMap17():    
    return render_template('Pune_Maps/Parvati Park.html') 

@app.route('/PMap18', methods=['POST','GET'])
def PuneMap18():    
    return render_template('Pune_Maps/Pune Junction.html') 

@app.route('/PMap19', methods=['POST','GET'])
def PuneMap19():    
    return render_template('Pune_Maps/Salunkhe Vihar Road.html') 

@app.route('/PMap20', methods=['POST','GET'])
def PuneMap20():    
    return render_template('Pune_Maps/Satara Road.html') 

@app.route('/PMap21', methods=['POST','GET'])
def PuneMap21():    
    return render_template('Pune_Maps/Shaniwar Wada.html') 

@app.route('/PMap22', methods=['POST','GET'])
def PuneMap22():    
    return render_template('Pune_Maps/Shivaji Nagar.html')

@app.route('/PMap23', methods=['POST','GET'])
def PuneMap23():    
    return render_template('Pune_Maps/Shri Krishna Nagar.html') 

@app.route('/PMap24', methods=['POST','GET'])
def PuneMap24():    
    return render_template('Pune_Maps/Shukrawar Peth.html') 

@app.route('/PMap25', methods=['POST','GET'])
def PuneMap25():    
    return render_template('Pune_Maps/Somvar Peth.html')

@app.route('/PMap26', methods=['POST','GET'])
def PuneMap26():    
    return render_template('Pune_Maps/Viman Nagar.html')   


    
# =====================================
#  Chandigarh Data
# =====================================

@app.route('/loadMap2', methods=['POST','GET'])

def chd():
 
    
    return render_template('Chandigarhstreet.html')
    
@app.route('/CMap1', methods=['POST','GET'])
def ChdMap1():
     return render_template('Chandigarh_Maps/CCET.html')

@app.route('/CMap2', methods=['POST','GET'])
def ChdMap2():
     return render_template('Chandigarh_Maps/Cactus Garden.html')
     
@app.route('/CMap3', methods=['POST','GET'])
def ChdMap3():
     return render_template('Chandigarh_Maps/Elante Mall.html')
     
@app.route('/CMap4', methods=['POST','GET'])
def ChdMap4():
     return render_template('Chandigarh_Maps/Maya Hotel.html')     

@app.route('/CMap5', methods=['POST','GET'])
def ChdMap5():
     return render_template('Chandigarh_Maps/Panjab University.html')

@app.route('/CMap6', methods=['POST','GET'])
def ChdMap6():
     return render_template('Chandigarh_Maps/Sector 7.html')

@app.route('/CMap7', methods=['POST','GET'])
def ChdMap7():
     return render_template('Chandigarh_Maps/Sector 10.html')

@app.route('/CMap8', methods=['POST','GET'])
def ChdMap8():
     return render_template('Chandigarh_Maps/Sector 15.html')

@app.route('/CMap9', methods=['POST','GET'])
def ChdMap9():
     return render_template('Chandigarh_Maps/Sector 17.html')

@app.route('/CMap10', methods=['POST','GET'])
def ChdMap10():
     return render_template('Chandigarh_Maps/Sector 22.html')

@app.route('/CMap11', methods=['POST','GET'])
def ChdMap11():
     return render_template('Chandigarh_Maps/Sector 26.html') 

@app.route('/CMap12', methods=['POST','GET'])
def ChdMap12():
     return render_template('Chandigarh_Maps/Sector 28.html')  

@app.route('/CMap13', methods=['POST','GET'])
def ChdMap13():
     return render_template('Chandigarh_Maps/Sector 35.html')

@app.route('/CMap14', methods=['POST','GET'])
def ChdMap14():
     return render_template('Chandigarh_Maps/Sector 38.html') 

@app.route('/CMap15', methods=['POST','GET'])
def ChdMap15():
     return render_template('Chandigarh_Maps/Sector 40.html')    
     
     
     
     
# =====================================
#  Bangalore Data
# =====================================

@app.route('/loadMap3', methods=['POST','GET'])

def BangMap():
    return render_template('bangalorestreet.html')
# =====================================

@app.route('/BMap1', methods=['POST','GET'])
def BangMap1():    
    return render_template('Bangalore_Maps/Ashok Nagar.html')

@app.route('/BMap2', methods=['POST','GET'])
def BangMap2():    
    return render_template('Bangalore_Maps/Banaswadi.html')    

@app.route('/BMap3', methods=['POST','GET'])
def BangMap3():    
    return render_template('Bangalore_Maps/Bangalore Cantonment.html')

@app.route('/BMap4', methods=['POST','GET'])
def BangMap4():    
    return render_template('Bangalore_Maps/Bangalore East Rail Station.html')

@app.route('/BMap5', methods=['POST','GET'])
def BangMap5():    
    return render_template('Bangalore_Maps/Bangalore West.html')

@app.route('/BMap6', methods=['POST','GET'])
def BangMap6():    
    return render_template('Bangalore_Maps/Basavanagudi.html')

@app.route('/BMap7', methods=['POST','GET'])
def BangMap7():    
    return render_template('Bangalore_Maps/Defence Colony.html')

@app.route('/BMap8', methods=['POST','GET'])
def BangMap8():    
    return render_template('Bangalore_Maps/DK Naik Nagar.html')

@app.route('/BMap9', methods=['POST','GET'])
def BangMap9():    
    return render_template('Bangalore_Maps/Field Marshall Kariappa Road.html')

@app.route('/BMap10', methods=['POST','GET'])
def BangMap10():    
    return render_template('Bangalore_Maps/Frazer Town.html')

@app.route('/BMap11', methods=['POST','GET'])
def BangMap11():    
    return render_template('Bangalore_Maps/Gandhi Nagar.html')

@app.route('/BMap12', methods=['POST','GET'])
def BangMap12():    
    return render_template('Bangalore_Maps/Goverment Technical Indus Institute.html')

@app.route('/BMap13', methods=['POST','GET'])
def BangMap13():    
    return render_template('Bangalore_Maps/IIM Bangalore.html') 

@app.route('/BMap14', methods=['POST','GET'])
def BangMap14():    
    return render_template('Bangalore_Maps/Indira Nagar.html') 

@app.route('/BMap15', methods=['POST','GET'])
def BangMap15():    
    return render_template('Bangalore_Maps/ITI Industrial Estate.html') 

@app.route('/BMap16', methods=['POST','GET'])
def BangMap16():    
    return render_template('Bangalore_Maps/JP Nagar.html') 

@app.route('/BMap17', methods=['POST','GET'])
def BangMap17():    
    return render_template('Bangalore_Maps/Kalyan Nagar.html') 

@app.route('/BMap18', methods=['POST','GET'])
def BangMap18():    
    return render_template('Bangalore_Maps/Koramangala.html') 

@app.route('/BMap19', methods=['POST','GET'])
def BangMap19():    
    return render_template('Bangalore_Maps/Madhav Nagar.html') 

@app.route('/BMap20', methods=['POST','GET'])
def BangMap20():    
    return render_template('Bangalore_Maps/Madras Engineers group.html') 

@app.route('/BMap21', methods=['POST','GET'])
def BangMap21():    
    return render_template('Bangalore_Maps/Mahadevapura.html') 

@app.route('/BMap22', methods=['POST','GET'])
def BangMap22():    
    return render_template('Bangalore_Maps/Mantri Square.html')

@app.route('/BMap23', methods=['POST','GET'])
def BangMap23():    
    return render_template('Bangalore_Maps/Marathahalli.html') 

@app.route('/BMap24', methods=['POST','GET'])
def BangMap24():    
    return render_template('Bangalore_Maps/Marenahalli.html') 

@app.route('/BMap25', methods=['POST','GET'])
def BangMap25():    
    return render_template('Bangalore_Maps/Mill Corner Road.html')

@app.route('/BMap26', methods=['POST','GET'])
def BangMap26():    
    return render_template('Bangalore_Maps/MSR Nagar.html')
    
@app.route('/BMap27', methods=['POST','GET'])
def BangMap27():    
    return render_template('Bangalore_Maps/MSRIT Road.html') 

@app.route('/BMap28', methods=['POST','GET'])
def BangMap28():    
    return render_template('Bangalore_Maps/Nehru Road.html') 

@app.route('/BMap29', methods=['POST','GET'])
def BangMap29():    
    return render_template('Bangalore_Maps/Old Madras Road.html') 

@app.route('/BMap30', methods=['POST','GET'])
def BangMap30():    
    return render_template('Bangalore_Maps/Outer Ring Road.html') 

@app.route('/BMap31', methods=['POST','GET'])
def BangMap31():    
    return render_template('Bangalore_Maps/Phoenix Mall.html')
    
@app.route('/BMap32', methods=['POST','GET'])
def BangMap32():    
    return render_template('Bangalore_Maps/Richard Town.html')

@app.route('/BMap33', methods=['POST','GET'])
def BangMap33():    
    return render_template('Bangalore_Maps/Sadaramangala.html') 

@app.route('/BMap34', methods=['POST','GET'])
def BangMap34():    
    return render_template('Bangalore_Maps/Shantala Nagar.html') 

@app.route('/BMap35', methods=['POST','GET'])
def BangMap35():    
    return render_template('Bangalore_Maps/St. Annes Womens College.html') 

@app.route('/BMap36', methods=['POST','GET'])
def BangMap36():    
    return render_template('Bangalore_Maps/Sudhama Nagar.html')

@app.route('/BMap37', methods=['POST','GET'])
def BangMap37():    
    return render_template('Bangalore_Maps/Trinity Mall.html') 

@app.route('/BMap38', methods=['POST','GET'])
def BangMap38():    
    return render_template('Bangalore_Maps/Vijpana Nagar.html')

@app.route('/BMap39', methods=['POST','GET'])
def BangMap39():    
    return render_template('Bangalore_Maps/Wilson Gardens.html')

    
# =====================================
#  Mumbai Data
# =====================================

@app.route('/loadMap4', methods=['POST','GET'])

def MumbaiMap():
    return render_template('Mumbaistreet.html')
    
    
    
@app.route('/MMap1', methods=['POST','GET'])
def MumbaiMap1():    
    return render_template('Mumbai_Maps/Antop Hill.html')

@app.route('/MMap2', methods=['POST','GET'])
def MumbaiMap2():    
    return render_template('Mumbai_Maps/Ballard Estate.html')    

@app.route('/MMap3', methods=['POST','GET'])
def MumbaiMap3():    
    return render_template('Mumbai_Maps/Bora Bazaar.html')

@app.route('/MMap4', methods=['POST','GET'])
def MumbaiMap4():    
    return render_template('Mumbai_Maps/Bori Bunder.html')

@app.route('/MMap5', methods=['POST','GET'])
def MumbaiMap5():    
    return render_template('Mumbai_Maps/Borivali.html')

@app.route('/MMap6', methods=['POST','GET'])
def MumbaiMap6():    
    return render_template('Mumbai_Maps/Chhatrapati Shivaji Terminus.html')

@app.route('/MMap7', methods=['POST','GET'])
def MumbaiMap7():    
    return render_template('Mumbai_Maps/Chium Village.html')

@app.route('/MMap8', methods=['POST','GET'])
def MumbaiMap8():    
    return render_template('Mumbai_Maps/Cooperage.html')

@app.route('/MMap9', methods=['POST','GET'])
def MumbaiMap9():    
    return render_template('Mumbai_Maps/Cusrow Baug.html')

@app.route('/MMap10', methods=['POST','GET'])
def MumbaiMap10():    
    return render_template('Mumbai_Maps/Dalal Street.html')

@app.route('/MMap11', methods=['POST','GET'])
def MumbaiMap11():    
    return render_template('Mumbai_Maps/Dr Annie besent Road.html')

@app.route('/MMap12', methods=['POST','GET'])
def MumbaiMap12():    
    return render_template('Mumbai_Maps/Ganesh Lane.html')

@app.route('/MMap13', methods=['POST','GET'])
def MumbaiMap13():    
    return render_template('Mumbai_Maps/Gateway Of India.html') 

@app.route('/MMap14', methods=['POST','GET'])
def MumbaiMap14():    
    return render_template('Mumbai_Maps/Goregaon East.html') 

@app.route('/MMap15', methods=['POST','GET'])
def MumbaiMap15():    
    return render_template('Mumbai_Maps/Goregaon West.html') 

@app.route('/MMap16', methods=['POST','GET'])
def MumbaiMap16():    
    return render_template('Mumbai_Maps/Guru Nanak Khalsa College.html') 

@app.route('/MMap17', methods=['POST','GET'])
def MumbaiMap17():    
    return render_template('Mumbai_Maps/Hutatma Chowk.html') 

@app.route('/MMap18', methods=['POST','GET'])
def MumbaiMap18():    
    return render_template('Mumbai_Maps/Institute Of Chemical Technology.html') 

@app.route('/MMap19', methods=['POST','GET'])
def MumbaiMap19():    
    return render_template('Mumbai_Maps/Kala Ghoda.html') 

@app.route('/MMap20', methods=['POST','GET'])
def MumbaiMap20():    
    return render_template('Mumbai_Maps/Loadha Park.html') 

@app.route('/MMap21', methods=['POST','GET'])
def MumbaiMap21():    
    return render_template('Mumbai_Maps/Lokhandwala.html') 

@app.route('/MMap22', methods=['POST','GET'])
def MumbaiMap22():    
    return render_template('Mumbai_Maps/M.G Road.html')

@app.route('/MMap23', methods=['POST','GET'])
def MumbaiMap23():    
    return render_template('Mumbai_Maps/Matunga East.html') 

@app.route('/MMap24', methods=['POST','GET'])
def MumbaiMap24():    
    return render_template('Mumbai_Maps/MT Vilas Rao Road.html') 

@app.route('/MMap25', methods=['POST','GET'])
def MumbaiMap25():    
    return render_template('Mumbai_Maps/Nariman Point.html')

@app.route('/MMap26', methods=['POST','GET'])
def MumbaiMap26():    
    return render_template('Mumbai_Maps/Peninsula Buissness Park.html')
    
@app.route('/MMap27', methods=['POST','GET'])
def MumbaiMap27():    
    return render_template('Mumbai_Maps/Ram Mandir Station.html') 

@app.route('/MMap28', methods=['POST','GET'])
def MumbaiMap28():    
    return render_template('Mumbai_Maps/Santa Cruz.html') 

@app.route('/MMap29', methods=['POST','GET'])
def MumbaiMap29():    
    return render_template('Mumbai_Maps/Senapati Bapat Marg.html') 

@app.route('/MMap30', methods=['POST','GET'])
def MumbaiMap30():    
    return render_template('Mumbai_Maps/SPM Chowk.html') 

@app.route('/MMap31', methods=['POST','GET'])
def MumbaiMap31():    
    return render_template('Mumbai_Maps/SPM Road.html')
    
@app.route('/MMap32', methods=['POST','GET'])
def MumbaiMap32():    
    return render_template('Mumbai_Maps/Vitthalbhai Patel Road.html')

@app.route('/MMap33', methods=['POST','GET'])
def MumbaiMap33():    
    return render_template('Mumbai_Maps/VJTI.html') 

@app.route('/MMap34', methods=['POST','GET'])
def MumbaiMap34():    
    return render_template('Mumbai_Maps/YMCA Road.html') 



@app.route('/about', methods=['POST','GET'])

def About():
 
    
    return render_template('about.html')
    
@app.route('/locator', methods=['POST','GET'])

def Loc(): 
    return render_template('locator.html')
    
@app.route('/coord', methods=['POST','GET'])

def Coord(): 
    return render_template('Category.html')    

# api json 
@app.route('/sum', methods=['GET','POST'])
def sum():
    sum = 0
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = a+b
    return jsonify(sum)

if __name__ == '__main__':
    app.run(debug=True)