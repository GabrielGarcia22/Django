document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const body = document.body;

    // Función para aplicar el tema basado en el estado almacenado
    const applyTheme = () => {
        const savedTheme = localStorage.getItem('theme') || 'light-mode'; // Por defecto, modo claro
        if (savedTheme === 'dark-mode') {
            body.classList.replace('light-mode', 'dark-mode');
            toggleButton.innerHTML = '<i class="bi bi-sun" style="color: #FFFFFF;"></i>'; // Sol en modo oscuro
        } else {
            body.classList.replace('dark-mode', 'light-mode');
            toggleButton.innerHTML = '<i class="bi bi-moon" style="color: #000000;"></i>'; // Luna en modo claro
        }
    };

    // Aplicar el tema al cargar la página
    applyTheme();

    // Función para alternar el tema
    const toggleTheme = () => {
        if (body.classList.contains('light-mode')) {
            body.classList.replace('light-mode', 'dark-mode');
            toggleButton.innerHTML = '<i class="bi bi-sun" style="color: #FFFFFF;"></i>';
            localStorage.setItem('theme', 'dark-mode'); // Guardar modo oscuro
        } else {
            body.classList.replace('dark-mode', 'light-mode');
            toggleButton.innerHTML = '<i class="bi bi-moon" style="color: #000000;"></i>';
            localStorage.setItem('theme', 'light-mode'); // Guardar modo claro
        }
    };

    // ClicK en el botón
    toggleButton.addEventListener('click', toggleTheme);


    // Manejar el envío del formulario
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Evitar el envío por defecto

            emailjs.sendForm('TU_SERVICE_ID', 'TU_TEMPLATE_ID', contactForm)
                .then(() => {
                    document.getElementById('form-message').textContent = 'Mensaje enviado con éxito!';
                    document.getElementById('form-message').style.color = 'green';
                    contactForm.reset(); // Limpiar el formulario
                }, (error) => {
                    document.getElementById('form-message').textContent = 'Error al enviar el mensaje: ' + error.text;
                    document.getElementById('form-message').style.color = 'red';
                });
        });
    }

    // Función sendMail
    window.sendMail = function() {
        const email = document.getElementById("email").value;
        if (email) {
            window.location.href = `mailto:${email}?subject=Consulta%20sobre%20SleepBetter`;
            alert('Correo enviado');
        } else {
            alert('Por favor ingresa un correo');
        }
    };
}); 