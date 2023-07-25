function changePassword() {
  document.getElementById("changePassword").classList.toggle("active");
  $('body').addClass('overflow-hidden');
}

function closeModal() {
  $('body').removeClass('overflow-hidden');
}

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("change-password");

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission

    var url = form.action;
    var formData = new FormData(form);

    fetch(url, {
        method: "POST",
        body: formData
      })
      .then(function (response) {
        if (response.status === 400) {
          return response.json();
        } else {
          Swal.fire({
            icon: 'success',
            title: 'Password already changed!',
            showConfirmButton: false,
            timer: 1500
          });
          setTimeout(function () {
            // Reload the current page
            location.reload();
          }, 2000);
        }
      })
      .then(function (errors) {
        document.getElementById("old_password_err").innerText = ""
        document.getElementById("new_password2_err").innerText = ""
        document.getElementById("new_password1_err").innerText = ""

        if (errors.hasOwnProperty('old_password')) {
          document.getElementById("old_password_err").innerText = errors.old_password[0].message
        }
        if (errors.hasOwnProperty('new_password2')) {
          document.getElementById("new_password2_err").innerText = errors.new_password2[0].message
        }
        if (errors.hasOwnProperty('new_password1')) {
          document.getElementById("new_password1_err").innerText = errors.new_password1[0].message
        }
      })
      .catch(function (error) {
        // Handle network or other errors
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("editProfile");

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission

    var url = form.action;
    var formData = new FormData(form);

    fetch(url, {
        method: "POST",
        body: formData
      })
      .then(function (response) {
        if (response.status === 400) {
          return response.json();
        } else {
          Swal.fire({
            icon: 'success',
            title: 'Profile already updated!',
            showConfirmButton: false,
            timer: 1500
          });
          setTimeout(function () {
            // Reload the current page
            location.reload();
          }, 2000);
        }
      })
      .then(function (errors) {
        document.getElementById("avatar_err").innerText = ""
        document.getElementById("name_err").innerText = ""

        if (errors.hasOwnProperty('avatar')) {
          document.getElementById("avatar_err").innerText = errors.avatar[0].message
        }
        if (errors.hasOwnProperty('first_name')) {
          document.getElementById("name_err").innerText = errors.first_name[0].message
        }
        // Form submission failed, show error popup
        Swal.fire({
          icon: 'error',
          title: 'Profile update failed',
          showConfirmButton: false,
          timer: 3000
        });
      })
      .catch(function (error) {
        // Handle network or other errors
      });
  });
});