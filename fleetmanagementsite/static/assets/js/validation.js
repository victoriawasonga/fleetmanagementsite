

window.onload=function(){
    const license_no_field=document.querySelector('#id_license_no');
    const feedback_area=document.querySelector('.invalid-feedback')
    license_no_field.addEventListener("keyup", (e) => {
    console.log("777777",777777);
    const license_no_val=e.target.value;
    console.log("license_no_val",license_no_val);
    if(license_no_val.length>0){
        fetch('/fleetmanagement/validate_license',{
            body:JSON.stringify({
                'license_no':license_no_val}),
                method:'POST',
        })
        .then(res=>res.json())
        .then(data=>{
            console.log("data",data);
            if(data.license_no_error){
                license_no_field.classList.add("is-invalid");
                feedback_area.style.display="block";
                feedback_area.innerHTML=`<p>${data.license_no_error}</p>`
            }

        });

    }

});

}