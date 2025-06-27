var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["facName"] = document.getElementById("facName").value;
  formData["facDep"] = document.getElementById("facAge").value;
  formData["facSub"] = document.getElementById("facMobileNo").value;
  formData["facAge"] = document.getElementById("facEmail id").value;
  formData["facPlace"] = document.getElementById("facCourse").value;
  return formData;
}
function resetForm() {
  document.getElementById("facName").value = "";
  document.getElementById("facAge").value = "";
  document.getElementById("facMobileNo").value = "";
  document.getElementById("facEmail id").value = "";
  document.getElementById("facCourse").value = "";
  selectedRow = null;
}
function isValid(){
var a=document.getElementById("facName").value;
 var  b = document.getElementById("facAge").value;
 var c= document.getElementById("facMobileNo").value;
 var d= document.getElementById("facEmail id").value;
 var e= document.getElementById("facCourse").value;
if(ValidateName(a)){return true;}
else
{return false;}
}
function  ValidateName(a) {
const namePattern=/^[a-zA-Z\s'-]+$/;
return namePattern.test(a);
}

