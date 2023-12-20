// validating the admin page form 
var title = document.querySelector('.input-title');
var content = document.querySelector('#input-content');

console.log("Hello world");

function validateForm() {
    if (title == '' || content == '') {
        alert('Please fill all fields.');
        return false;
    }
    else if (title.length > 150) {
        alert("Please write title in '150 characters'.");
        return false;
    }

    return true;
}