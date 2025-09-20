import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from myfirepro.firebase_config import db

FIREBASE_KEY = "AIzaSyAMrry7cqeyQWOB__JoTbCJqAKsy2HuOBM"

def Register(request):
    if request.method=="POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        p = request.POST.get("password")
        pn = request.POST.get("phone_number")
        g = request.POST.get("gender")
        a = request.POST.get("address")

        if not n or not e or not p or not pn or not g or not a:
            messages.error("All Fields Required")
            return redirect("reg")
        if len(p) < 8:
            messages.error(request, "Password Must Be 8 Characters Long")
            return redirect("reg")

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_KEY}"
        payload = {

            "email": e,
            "password": p,

            "returnSecureToken":True
        }
        response = requests.post(url,payload)

        if response.status_code == 200:
            errorMsg = response.json()
        db.collection("registration").add({
            "Name" : n,
            "Email" : e,
            "Password" : p,
            "Phone" : pn,
            "Gender" : g,
            "Address" : a
        })
        messages.success(request, "User Has Been Register")
        return redirect("reg")

    return render(request,"myapp/userregistration.html")

def Showdata(request):
    reg_ref = db.collection("registration").stream()
    reg = []

    for doc in reg_ref:
        data = doc.to_dict()
        data['id'] = doc.id   # Add the document ID
        reg.append(data)

    return render(request, "myapp/showdata.html", {"reg": reg})


def delete(req,id):
    db.collection("registration").document(id).delete()
    return redirect("show")

