from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signupp,Detail,Rdetail,Odetail,Odetail2,Hdetail,Hdetail2,Detail2,Quick,Rdetail2,Edit,Recreq,Donreq,Orgreq,Hosreq,Rhosreq,Rdonreq,Rorgreq,Odonreq,Orecreq,Ohosreq,Hdonreq,Hrecreq,Horgreq

# Create your views here.
#global val

global val
def home(request):
    return render(request, "index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']

        if Signupp.objects.filter(username=username).exists() or Signupp.objects.filter(email=email).exists():
            # messages.error(request,"User already exists")
            return render(request,"log.html")
            
        myprofile=Signupp(username=username,email=email,password=password,role=role)
        myprofile.save()
        # messages.success(request,"Your account has been created successfully")
        global val
        def val():
            return username
        if role=='Organisation User':
            return render(request,"odetails.html")
        elif role=='Hospital User':
            return render(request,"hdetails.html")
        elif role=='Donor User':
            return render(request,"ddetails.html")
        elif role=='Receiver User':
            return render(request,"rdetails.html")
        else:
            # messages.error(request,"Invalid Role")
            return redirect('home')
    
    return render(request,"signup.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        global val
        def val():
            return username
        credential=Signupp.objects.all()
        flag=0
        for i in credential:
            if i.username==username and i.password==password :
                if i.role=='Receiver User':
                    flag=1
                    
                    def val():
                        return username
                
                    return render(request,"rdashboard.html")
                if i.role=='Donor User':
                    flag=1
                    def val():
                        return username
                
                    return render(request,"dashboard.html")
                if i.role=='Hospital User':
                    flag=1
                    #global val
                    def val():
                        return username
                
                    return render(request,"hdashboard.html")
                if i.role=='Organisation User':
                    flag=1
                    #global val
                    def val():
                        return username
                
                    return render(request,"odashboard.html")
        if flag==0:
            # messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"log.html")

def adminlogin(request):
    def val():
        return username

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'idonate' and password == 'idonate':
            username = val()
            return render(request, "admindash.html")
        else:
            context = {
                'error_message': 'Wrong Credentials'
            }
            return render(request, 'index.html', context)

    return render(request, "adminlogin.html")



def admin_home(request):
    return render(request,"admindash.html")



def signout(request):
    # messages.success(request,"Logged Out successfully!")
    return redirect('home')

def dashboard(request):
    return render(request,"dashboard.html")

def rdashboard(request):
    return render(request,"rdashboard.html")


def odashboard(request):
    return render(request,"odashboard.html")

def hdashboard(request):
    return render(request,"hdashboard.html")

def qdashboard(request):
    return render(request,"qdashboard.html")


def admindash(request):
    return render(request,"admindash.html")

def admdonar(request):
    return render(request,"admdonar.html")

def admrec(request):
    return render(request,"admrec.html")

def admorg(request):
    return render(request,"admorg.html")

def admhos(request):
    return render(request,"admhos.html")

def detail(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mobno = request.POST['mobno']
        ge = request.POST['ge']
        age = request.POST['age']
        bg = request.POST['bg']
        address = request.POST['address']
        occupation = request.POST['occupation']
        weight = request.POST['weight']
        height = request.POST['height']
        an = request.POST['an']
        tmr = request.POST['tmr']
        ldd = request.POST['ldd']
        dbo = request.POST['dbo']
        if len(request.FILES) != 0:
            image = request.FILES['image']

        username=val()
        #messages.success(request, "Your account has created successfully")
        det = Detail(username=username, fullname=fullname, dob=dob, email=email, mobno=mobno, ge=ge, age=age, bg=bg, address=address, occupation=occupation, weight=weight, height=height, an=an, tmr=tmr, ldd=ldd, dbo=dbo, image=image)
        det.save()
        # messages.success(request, "Details added successfully")
        return render(request, "details2.html")
    
    return render(request, "ddetails.html")

def edit(request):
    if request.method == "POST":
        don_edit_email = request.POST['don_edit_email']
        don_edit_mobno = request.POST['don_edit_mobno']
        don_edit_address = request.POST['don_edit_address']
        don_edit_occupation = request.POST['don_edit_occupation']
        don_edit_weight = request.POST['don_edit_weight']
        don_edit_height = request.POST['don_edit_height']
        don_edit_an = request.POST['don_edit_an']
        don_edit_tmr = request.POST['don_edit_tmr']
        don_edit_ldd = request.POST['don_edit_ldd']
        don_edit_sid = request.POST['don_edit_sid']
        don_edit_eidn = request.POST['don_edit_eidn']
        if len(request.FILES) != 0:
            don_edit_dsbg = request.FILES['don_edit_dsbg']
        username=val()
        #messages.success(request, "Your account has created successfully")
        edit = Edit(don_edit_email = don_edit_email,don_edit_mobno = don_edit_mobno,don_edit_address = don_edit_address,don_edit_occupation = don_edit_occupation,don_edit_weight = don_edit_weight,don_edit_height = don_edit_height,don_edit_an = don_edit_an,don_edit_tmr=don_edit_tmr,don_edit_ldd = don_edit_ldd,don_edit_sid = don_edit_sid,don_edit_eidn = don_edit_eidn,don_edit_dsbg = don_edit_dsbg)
        edit.save()
        # messages.success(request, "Details added successfully")
        return render(request, "dashboard.html")
    
    return render(request, "edit.html")

    

def rdetail(request):
    if request.method == "POST":
        fname = request.POST['fname']
        rdob = request.POST['rdob']
        remail = request.POST['remail']
        rmobno = request.POST['rmobno']
        rge = request.POST['rge']
        rage = request.POST['rage']
        rbg = request.POST['rbg']
        raddress = request.POST['raddress']
        roccupation = request.POST['roccupation']
        rweight = request.POST['rweight']
        rheight = request.POST['rheight']
        ran = request.POST['ran']
        rtmr = request.POST['rtmr']
        rlrd = request.POST['rlrd']
        rdbo = request.POST['rdbo']
        
        if len(request.FILES) != 0:
            rimage = request.FILES['rimage']
        else:
            rimage = None

        username=val()


        rdet = Rdetail(username=username, fname=fname, rdob=rdob, remail=remail, rmobno=rmobno, rge=rge, rage=rage, rbg=rbg, raddress=raddress, roccupation=roccupation, rweight=rweight, rheight=rheight, ran=ran, rtmr=rtmr, rlrd=rlrd, rdbo=rdbo, rimage=rimage)
        rdet.save()
        # messages.success(request, "Details added successfully")
        return render(request, "rdetail2.html")
    
    return render(request, "rdetails.html")



def odetail(request):
    if request.method == "POST":
        ofname = request.POST['ofname']
        oemail = request.POST['oemail']
        omobno = request.POST['omobno']
        oaddress = request.POST['oaddress']
        if len(request.FILES) != 0:
            oimage = request.FILES['oimage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        odet = Odetail(username=username, ofname=ofname, oemail=oemail, omobno=omobno, oaddress=oaddress, oimage=oimage)
        odet.save()
        # messages.success(request, "Details added successfully")
        return render(request, "odetail2.html")

    return render(request, "odetails.html")


def odetail2(request):
    if request.method == "POST":
        olicenceid = request.POST['olicenceid']
        if len(request.FILES) != 0:
            oiimage = request.FILES['oiimage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        odet2 = Odetail2(username=username, olicenceid=olicenceid ,oiimage=oiimage)
        odet2.save()
        #messages.success(request, "Details added successfully")
        return render(request, "odashboard.html")

    return render(request, "odetail2.html")

def oprofile(request):

    username=val()
    user_profile=Odetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Odetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'oprofile.html',{'i':i,'j':j})

def oidentity(request):
    username=val()
    user_profile=Odetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Odetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'oidentity.html',{'i':i,'j':j})

def orgsearch(request, username):
    r_p = Odetail.objects.filter(username=username).first()
    r2_p = Odetail2.objects.filter(username=username).first()
    return render(request, 'oprofile.html', {'i': r_p,'j':r2_p})

def orgidentity(request, username):
    r_p = Odetail.objects.filter(username=username).first()
    r2_p = Odetail2.objects.filter(username=username).first()
    return render(request, 'oidentity.html', {'i': r_p,'j':r2_p})

def hossearch(request, username):
    r_p = Hdetail.objects.filter(username=username).first()
    r2_p = Hdetail2.objects.filter(username=username).first()
    return render(request, 'hprofile.html', {'i': r_p,'j':r2_p})

def hosidentity(request, username):
    r_p = Hdetail.objects.filter(username=username).first()
    r2_p = Hdetail2.objects.filter(username=username).first()
    return render(request, 'hidentity.html', {'i': r_p,'j':r2_p})


def admorgreq(request):

    up = Odetail.objects.all()
    up1 = Odetail2.objects.all()
    return render(request, 'admorgreq.html', {'up': up, 'up1': up1})

def admhosreq(request):

    up = Hdetail.objects.all()
    up1 = Hdetail2.objects.all()
    return render(request, 'admhosreq.html', {'up': up, 'up1': up1})




def hdetail(request):
    if request.method == "POST":
        hfname = request.POST['hfname']
        hemail = request.POST['hemail']
        hmobno = request.POST['hmobno']
        haddress = request.POST['haddress']
        bbp = request.POST['bbp']
        obp = request.POST['obp']
        if len(request.FILES) != 0:
            himage = request.FILES['himage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        hdet = Hdetail(username=username, hfname=hfname, hemail=hemail, hmobno=hmobno, haddress=haddress, bbp=bbp, obp=obp, himage=himage)
        hdet.save()
        # messages.success(request, "Details added successfully")
        return render(request, "hdetail2.html")

    return render(request, "hdetails.html")


def hdetail2(request):
    if request.method == "POST":
        hlicenceid = request.POST['hlicenceid']
        if len(request.FILES) != 0:
            hiimage = request.FILES['hiimage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        hdet2 = Hdetail2(username=username, hlicenceid=hlicenceid ,hiimage=hiimage)
        hdet2.save()
        #messages.success(request, "Details added successfully")
        return render(request, "hdashboard.html")

    return render(request, "hdetail2.html")

def hprofile(request):
    username=val()
    user_profile=Hdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Hdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'hprofile.html',{'i':i,'j':j})

def hidentity(request):
    username=val()
    user_profile=Hdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Hdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'hidentity.html',{'i':i,'j':j})



def detail2(request):
    username=val()

    if request.method == "POST":
        sid = request.POST['sid']
        eidn = request.POST['eidn']
        if len(request.FILES) != 0:
            dsbg = request.FILES['dsbg']
        
        username=val()

        #messages.success(request, "Your account has created successfully")
        det2 = Detail2(username=username, sid=sid, eidn=eidn, dsbg=dsbg)
        det2.save()
        # messages.success(request, "Details added successfully")
        return render(request, "dashboard.html")
    
    return render(request, "details2.html")



def rdetail2(request):
    if request.method == "POST":
        rsid = request.POST['rsid']
        reidn = request.POST['reidn']
        if len(request.FILES) != 0:
            rdsbg = request.FILES['rdsbg']

        username=val()


        rdet2 = Rdetail2(username=username, rsid=rsid, reidn=reidn, rdsbg=rdsbg)
        rdet2.save()
        # messages.success(request, "Details added successfully")
        return render(request, "rdashboard.html")
    
    return render(request, "rdetail2.html")



def quick(request):
    if request.method=="POST":
        qfname=request.POST['qfname']
        qemail=request.POST['qemail']
        qmobno=request.POST['qmobno']
        qaddress=request.POST['qaddress']
       


        #messages.success(request,"Your account has created successfully")
        detq=Quick(qfname=qfname,qemail=qemail,qmobno=qmobno,qaddress=qaddress)
        detq.save()
        # messages.success(request,"Details added successfully")
        return render(request,"qdashboard.html")
    return render(request, "quick.html")


def profile(request):
    
    username=val()
    user_profile=Detail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Detail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'profile.html',{'i':i,'j':j})



def didentity(request):
    username=val()
    user_profile=Detail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Detail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'didentity.html',{'i':i,'j':j})


def donidentity(request, username):
    d_p = Detail.objects.filter(username=username).first()
    d2_p=Detail2.objects.filter(username=username).first()
    return render(request, 'didentity.html', {'i': d_p,'j':d2_p})

def doncontact(request, username):
    d_p = Detail.objects.filter(username=username).first()
    d2_p=Detail2.objects.filter(username=username).first()
    return render(request, 'dcontact.html', {'i': d_p,'j':d2_p})


def dcontact(request):
    username=val()
    user_profile=Detail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Detail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'dcontact.html',{'i':i,'j':j})


def rprofile(request):

    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Rdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'rprofile.html',{'i':i,'j':j})

def ridentity(request):

    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Rdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'ridentity.html',{'i':i,'j':j})


def rcontact(request):

    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Rdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'rcontact.html',{'i':i,'j':j})


def recidentity(request, username):
    r_p = Rdetail.objects.filter(username=username).first()
    r2_p = Rdetail2.objects.filter(username=username).first()
    return render(request, 'ridentity.html', {'i': r_p,'j':r2_p})


def reccontact(request, username):
    r_p = Rdetail.objects.filter(username=username).first()
    r2_p = Rdetail2.objects.filter(username=username).first()
    return render(request, 'rcontact.html', {'i': r_p,'j':r2_p})



def recsearch(request, username):
    r_p = Rdetail.objects.filter(username=username).first()
    r2_p = Rdetail2.objects.filter(username=username).first()
    return render(request, 'rprofile.html', {'i': r_p,'j':r2_p})




def donacceptreject(request, username):
    def don_delete_user_data(username):
        try:
            user_detail = Detail.objects.filter(username=username).first()
            if user_detail:
                user_detail.delete()
            user_signup = Signupp.objects.filter(username=username).first()
            if user_signup:
                user_signup.delete()
            user_detail2 = Detail2.objects.filter(username=username).first()
            if user_detail2:
                user_detail2.delete()
            return True
        except Exception as e:
            print(e)
            return False
    d_p = Detail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if don_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admdonreq")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admDacceptreject.html', {'i': d_p})


def recacceptreject(request, username):
    def rec_delete_user_data(username):
        try:
            user_detail = Rdetail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Rdetail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Rdetail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if rec_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admrecreq")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admRacceptreject.html', {'i': d_p})


def orgacceptreject(request, username):
    def org_delete_user_data(username):
        try:
            user_detail = Odetail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Odetail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Odetail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if org_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admorgreq")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admOacceptreject.html', {'i': d_p})

def hosacceptreject(request, username):
    def hos_delete_user_data(username):
        try:
            user_detail = Hdetail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Hdetail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Hdetail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if hos_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:

                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admhosreq")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admHacceptreject.html', {'i': d_p})



def donsearch(request, username):
    d_p = Detail.objects.filter(username=username).first()
    d2_p=Detail2.objects.filter(username=username).first()
    return render(request, 'profile.html', {'i': d_p,'j':d2_p})


def admdonreq(request):

    up = Detail.objects.all()
    up1 = Detail2.objects.all()
    return render(request, 'admdonreq.html', {'up': up, 'up1': up1})



def admrecreq(request):
 
 rd=Rdetail.objects.all()
 rd1=Rdetail2.objects.all()

 return render(request,'admrecreq.html',{'rd':rd,'rd1':rd1})

def qdon(request):
    # username=val()
    rd=Detail.objects.all()
    return render(request,'qdon.html',{'rd':rd})

def hqdon(request):
    # username=val()
    rd=Detail.objects.all()
    return render(request,'hqdon.html',{'rd':rd})

def oqdon(request):
    # username=val()
    rd=Detail.objects.all()
    return render(request,'oqdon.html',{'rd':rd})

def rqdon(request):
    # username=val()
    rd=Detail.objects.all()
    return render(request,'rqdon.html',{'rd':rd})

def qrec(request):
    # username=val()
    rd=Rdetail.objects.all()
    return render(request,'qrec.html',{'rd':rd})

def hqrec(request):
    # username=val()
    rd=Rdetail.objects.all()
    return render(request,'hqrec.html',{'rd':rd})

def oqrec(request):
    # username=val()
    rd=Rdetail.objects.all()
    return render(request,'oqrec.html',{'rd':rd})


def qorg(request):
    # username=val()
    up=Odetail.objects.all()
    return render(request,'qorg.html',{'up':up})

def hqorg(request):
    # username=val()
    up=Odetail.objects.all()
    return render(request,'hqorg.html',{'up':up})

def rqorg(request):
    # username=val()
    up=Odetail.objects.all()
    return render(request,'rqorg.html',{'up':up})

def qhos(request):
    # username=val()
    up=Hdetail.objects.all()
    return render(request,'qhos.html',{'up':up})

def oqhos(request):
    # username=val()
    up=Hdetail.objects.all()
    return render(request,'oqhos.html',{'up':up})

def rqhos(request):
    # username=val()
    up=Hdetail.objects.all()
    return render(request,'rqhos.html',{'up':up})

# def dsearch(request):
#     if request.method == 'POST':
#         username = request.POST.get('username') # Get donor's username from request
#         # Update the request status in your model or database
#         try:
#             donor = Rdetail.objects.get(username=username)
#             donor.status = True # Update request status to True
#             donor.save()
#             messages.success(request, 'Request sent successfully.') # Add success message
#         except Rdetail.DoesNotExist:
#             messages.error(request, 'Donor not found.') # Add error message if donor not found
#         return redirect('dashboard') # Redirect to dsearch view after updating request status

#     dsear = Rdetail.objects.all()
#     return render(request, 'dsearch.html', {'dsear': dsear})
def dsearch(request):
    return render(request,'dsearch.html')

def rsearch(request):
    return render(request,'rsearch.html')

def osearch(request):
    return render(request,'osearch.html')

def hsearch(request):
    return render(request,'hsearch.html')

def recreq(request):
    global val
    rd = Rdetail.objects.all()

    if request.method == "POST":
        scor = request.POST['scor']

        for r in rd:
            recusername = r.username  # Retrieve the username from each Rdetail object in the queryset
            username = val()
            recreq = Recreq(username=username, scor=scor, recusername=recusername)
            recreq.save()
        
        return render(request, "dsearch.html")
    
    return render(request, "recreq.html", {'rd': rd})


def orecreq(request):
    global val
    ord = Rdetail.objects.all()
    if request.method == "POST":
        Org_req_to_rec = request.POST['Org_req_to_rec']
        for rr in ord:
            orecusername = rr.username 
        username=val()
        orecreq = Orecreq(username=username, Org_req_to_rec=Org_req_to_rec,orecusername=orecusername)
        orecreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "osearch.html")
    
    return render(request, "orecreq.html", {'ord': ord})

def hrecreq(request):
    global val
    hrd = Rdetail.objects.all()
    if request.method == "POST":
        hsl_req_to_rec = request.POST['hsl_req_to_rec']
        for rr in hrd:
            hrecusername = rr.username 
            username=val()
            hrecreq = Hrecreq(username=username, hsl_req_to_rec=hsl_req_to_rec,hrecusername=hrecusername)
            hrecreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "hsearch.html")
    
    return render(request, "hrecreq.html", {'hrd': hrd})



def orgreq(request):
    global val
    od = Odetail.objects.all()

    if request.method == "POST":
        request = request.POST['request']
        for o in od:
            orgusername = o.username  # Retrieve the username from each Odetail object in the queryset
            
            username=val()
            orgreq = Orgreq(username=username, request=request, orgusername=orgusername)
            orgreq.save()
        # messages.success(request, "Details added successfully")
        return redirect('dsearch')
    return render(request, "orgreq.html",{'od': od})

# def hosreq(request):
#     global val
#     if request.method == "POST":
#         request_for = request.POST['request_for']
#         username=val()
#         hosreq = Hosreq(username=username, request_for=request_for)
#         hosreq.save()
#         # messages.success(request, "Details added successfully")
#         return render(request, "dsearch.html")
#     return render(request, "hosreq.html")

def hosreq(request):
    global val
    hd = Hdetail.objects.all()

    if request.method == "POST":
        requesth = request.POST['requesth']
        for h in hd:
            hosusername = h.username 
            username=val()
            dhosreq = Hosreq(username=username, requesth=requesth,hosusername=hosusername)
            dhosreq.save()
        # messages.success(request, "Details added successfully")
        return redirect('dsearch')

    return render(request, "hosreq.html",{'hd': hd})


def rdonreq(request):
    global val
    rdd = Detail.objects.all()
    if request.method == "POST":
        rec_req_to_donar = request.POST['rec_req_to_donar']
        for rd in rdd:
            rdonusername = rd.username
        username=val()
        rdonreq = Rdonreq(username=username, rec_req_to_donar=rec_req_to_donar,rdonusername=rdonusername)
        rdonreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "rsearch.html")
    return render(request, "rdonreq.html",{'rdd': rdd})

def odonreq(request):
    global val
    odd = Detail.objects.all()
    if request.method == "POST":
        org_req_to_donar = request.POST['org_req_to_donar']
        for od in odd:
            rdonusername = od.username
        username=val()
        odonreq = Odonreq(username=username, org_req_to_donar=org_req_to_donar,rdonusername=rdonusername)
        odonreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "osearch.html")
    return render(request, "odonreq.html",{'odd': odd})

def hdonreq(request):
    global val
    hdd = Detail.objects.all()
    if request.method == "POST":
        hospital_req_to_don = request.POST['hospital_req_to_don']
        for hd in hdd:
            hdonusername = hd.username
            username=val()
            hdonreq = Hdonreq(username=username, hospital_req_to_don=hospital_req_to_don,hdonusername=hdonusername)
            hdonreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "hsearch.html")
    return render(request, "hdonreq.html",{'hdd': hdd})


def rorgreq(request):
    global val
    rod = Odetail.objects.all()
    if request.method == "POST":
        rec_req_to_organization = request.POST['rec_req_to_organization']
        for ro in rod:
            rorgusername = o.username 
            username=val()
            rorgreq = Rorgreq(username=username, rec_req_to_organization=rec_req_to_organization,rorgusername=rorgusername)
            rorgreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "rsearch.html")
    return render(request, "rorgreq.html",{'rod': rod})

def horgreq(request):
    global val
    hrd = Rdetail.objects.all()
    if request.method == "POST":
        hsl_req_to_organization = request.POST['hsl_req_to_organization']
        for hr in hrd:
            hrecusername = hr.username 
            username=val()
            horgreq = Horgreq(username=username, hsl_req_to_organization=hsl_req_to_organization,hrecusername=hrecusername)
            horgreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "hsearch.html")
    return render(request, "horgreq.html", {'hrd': hrd})


def rhosreq(request):
    global val
    rhd = Hdetail.objects.all()

    if request.method == "POST":
        hosuserreq = request.POST['hosuserreq']
        for rh in rhd:
            rhosusername = rh.username
            username=val()
            rhosreq = Rhosreq(username=username, hosuserreq=hosuserreq,rhosusername=rhosusername)
            rhosreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "rsearch.html")
    return render(request, "rhosreq.html",{'rhd': rhd})

def ohosreq(request):
    global val
    ohd = Hdetail.objects.all()
    if request.method == "POST":
        org_req_to_hos = request.POST['org_req_to_hos']
        for oh in ohd:
            ohosusername = oh.username 
            username=val()
            ohosreq = Ohosreq(username=username, org_req_to_hos=org_req_to_hos,ohosusername=ohosusername)
            ohosreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "osearch.html")
    return render(request, "ohosreq.html",{'ohd': ohd})


def donreq(request):
    if request.method == "POST":
        scod = request.POST['scod']
        username=val()
        donreq = Donreq(username=username, scod=scod)
        donreq.save()
        # messages.success(request, "Details added successfully")
        return render(request, "dsearch.html")
    
    return render(request, "donreq.html")


def admorgreq(request):
    # username=val()
    up=Odetail.objects.all()
    return render(request,'admorgreq.html',{'up':up})

def admhosreq(request):
    # username=val()
    up=Hdetail.objects.all()
    return render(request,'admhosreq.html',{'up':up})

def rnotification(request):
    received_requests = Detail.objects.filter(email=request.user.email,)
    return render(request,'rnotification.html', {'received_requests': received_requests})  
