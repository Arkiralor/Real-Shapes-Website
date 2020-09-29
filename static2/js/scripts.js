function phonenumber(visphone) {
    var phoneno = /[0-9]{10}$/;
    if ((visphone.value.match(phoneno)) {
            return true;
        } else {
            alert("Invalid phone number, please add a valid mobile number.");
            return false;
        }
    }