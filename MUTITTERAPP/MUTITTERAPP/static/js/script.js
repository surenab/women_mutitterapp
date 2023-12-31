document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signup-button');
    const registrationFormContainer = document.getElementById('signup');
    registerButton.addEventListener('click', function() {
        history.pushState(null, '', '/accounts/register/');
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('login-button');
    const registrationFormContainer = document.getElementById('signup');
    registerButton.addEventListener('click', function() {
        history.pushState(null, '', '/accounts/login/');
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signup-button');
    const loginButton = document.getElementById('login-button');
    const signupFormContainer = document.getElementById('signup');
    const signupFormOriginalTransform = signupFormContainer.style.transform;
    let isMoving = false;

    registerButton.addEventListener('click', function(event) {
        if (!isMoving) {
            isMoving = true;
            signupFormContainer.style.transform = "translateY(-500px)";
            setTimeout(() => {
                isMoving = false;
            }, 800);
        }
        event.preventDefault();
    });
    loginButton.addEventListener('click', function(event) {
        if (!isMoving) {
            isMoving = true;
            signupFormContainer.style.transform = signupFormOriginalTransform;
            setTimeout(() => {
                isMoving = false;
            }, 800);
        }
        event.preventDefault();
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signup-button');
    const loginButton = document.getElementById('login-button');
    const signupFormContainer = document.getElementById('signup');
    const loginFormContainer = document.getElementById('login');
    const signupFormOriginalTransform = signupFormContainer.style.transform;
    const loginFormOriginalTransform = loginFormContainer.style.transform;
    let isMoving = false;

    registerButton.addEventListener('click', function(event) {
        if (!isMoving) {
            isMoving = true;
            signupFormContainer.style.transform = "translateY(-500px)";
            loginButton.style.fontSize = "2rem";
            registerButton.style.fontSize = "3rem";
            registerButton.style.marginBottom = "10px";
            setTimeout(() => {
                isMoving = false;
            }, 800);
        }
        event.preventDefault();
    });

    loginButton.addEventListener('click', function(event) {
        if (!isMoving) {
            isMoving = true;
            signupFormContainer.style.transform = signupFormOriginalTransform;
            loginButton.style.fontSize = "2.5rem";
            registerButton.style.fontSize = "2.5rem";
            registerButton.style.marginBottom = "50px";
            setTimeout(() => {
                isMoving = false;
            }, 800);
        }
        event.preventDefault();
    });
});
function toggleReplyForm(commentId) {
    var replyForm = document.getElementById('reply-form-' + commentId);
    if (replyForm.style.display === 'none' || !replyForm.style.display) {
        replyForm.style.display = 'block';
    } else {
        replyForm.style.display = 'none';
    }
    }

    function cancelReplyForm(commentId) {
    var replyForm = document.getElementById('reply-form-' + commentId);
    replyForm.style.display = 'none';
    }
    document.addEventListener('DOMContentLoaded', function() {
    const replyLinks = document.querySelectorAll('.reply-link');

    replyLinks.forEach(link => {
        link.addEventListener('click', function() {
            const commentId = this.getAttribute('data-comment-id');
            const replyForm = document.getElementById('reply-form-' + commentId);

            if (replyForm.style.display === 'none' || !replyForm.style.display) {
                replyForm.style.display = 'block';
            } else {
                replyForm.style.display = 'none';
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("id_image").addEventListener("change", function() {
        var selectedImageName = this.files[0] ? this.files[0].name : "Select your image";
        document.querySelector(".custom-file-label").textContent = selectedImageName;
    });
});
