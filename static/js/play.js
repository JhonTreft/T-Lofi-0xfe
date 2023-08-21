import { enviroments_url } from './config'

gustar_o_no = document.getElementById('song-saved')

if(localStorage.getItem('gustar') === 'true')
{
  gustar_o_no.classList.add('saved')
}else{
  gustar_o_no.classList.remove('saved')
}





  let theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';

if( theme == 'dark' ){
    document.documentElement.classList.add('dark')
}

document.getElementById('dark-mode-toggle').addEventListener('click', function(){
   document.documentElement.classList.toggle('dark')
});






var saveButton = document.getElementById('song-saved');

// Agregar un controlador de eventos para el evento "click"
saveButton.addEventListener('click', function() {
  if (saveButton.classList.contains('saved')) {
    // Si el botón ya tiene la clase "saved", eliminarla
    saveButton.classList.remove('saved');
    var xhr = new XMLHttpRequest();

    // Especificar la URL del servicio que maneja la actualización del campo, incluyendo el ID del objeto
    let id_song = document.getElementById('id_song').textContent;
    console.log("id",id_song)

    var url = `${enviroments_url}/api/not_song/` + id_song;

    console.log(url)

    // Configurar la petición con el método HTTP POST y los encabezados necesarios
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    // Agregar un controlador de eventos para manejar la respuesta de la petición
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // La petición fue exitosa, hacer algo con la respuesta
        console.log("Campo no gustar exitosamente");
      } else if (xhr.readyState === 4 && xhr.status !== 200) {
        // La petición falló, hacer algo con el error
        console.error("La petición falló con el código de estado " + xhr.status);
      }
    };

    localStorage.setItem('no_gustar_song_' + id_song, true);
    console.log("tenia que eliminar el gustar")
    localStorage.removeItem('gustar_song_' + id_song);

    // Enviar la petición sin parámetros
    xhr.send();
    // Código para desmarcar la canción como favorita
  } else {
    // Si el botón no tiene la clase "saved", agregarla
    saveButton.classList.add('saved');
    // Crear una nueva petición XHR
    var xhr = new XMLHttpRequest();

    // Especificar la URL del servicio que maneja la actualización del campo, incluyendo el ID del objeto
    let id_song = document.getElementById('id_song').textContent;


    var url = `${enviroments_url}/api/increment_zumba/` + id_song;

    console.log(url)

    // Configurar la petición con el método HTTP POST y los encabezados necesarios
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    // Agregar un controlador de eventos para manejar la respuesta de la petición
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // La petición fue exitosa, hacer algo con la respuesta
        console.log("Campo incrementado exitosamente");
      } else if (xhr.readyState === 4 && xhr.status !== 200) {
        // La petición falló, hacer algo con el error
        console.error("La petición falló con el código de estado " + xhr.status);
      }
    };
    localStorage.setItem('gustar_song_' + id_song, true);
    localStorage.removeItem('no_gustar_song_'+ id_song);

    // Enviar la petición sin parámetros
    xhr.send();
    // Código para marcar la canción como favorita
  }
});

    
setTimeout(function() {


  let spanElement = document.querySelector('.id_song');
  let id_song = spanElement.textContent



      // Función para obtener el ID de la canción desde una clave del localStorage
    function getIdFromLocalStorageKey(key) {
      const prefix = 'gustar_song_';
      if (key.startsWith(prefix)) {
        return key.slice(prefix.length);
      }
      return null;
    }

    // Variable para almacenar el resultado de la comparación
    let isLiked = false;

    // Iterar a través de todas las claves almacenadas en el localStorage
    for (let key in localStorage) {
      // Verificar si la clave comienza con 'gustar_song_'
      if (key.startsWith('gustar_song_')) {
        // Obtener el ID de la canción desde la clave actual
        const storedId = getIdFromLocalStorageKey(key);

        // Comparar el ID almacenado con el ID que tienes en la variable
        if (storedId === id_song) {
          gustar_o_no = document.getElementById('song-saved')
          gustar_o_no.classList.add('saved')
          isLiked = true
          // Si encuentras una coincidencia, puedes detener el bucle si lo deseas.
          // break;
        }
      }
    }

    // Después de la iteración, puedes utilizar la variable isLiked para saber si el ID de la canción que tienes en la variable se encuentra en el localStorage.
    if (isLiked) {
      console.log('La canción con el ID ' + id_song + ' le gusta al usuario.');
    } else {
      console.log('La canción con el ID ' + id_song + ' NO le gusta al usuario.');
    }


    localStorage.setItem("load_hearts",true)



}, 5000);




function getSongIdAfterDelay() {
  setTimeout(function() {
    let spanElement = document.querySelector('.id_song');
    let id_song = spanElement.textContent
  
  
  
        // Función para obtener el ID de la canción desde una clave del localStorage
      function getIdFromLocalStorageKey(key) {
        const prefix = 'gustar_song_';
        if (key.startsWith(prefix)) {
          return key.slice(prefix.length);
        }
        return null;
      }
  
      // Variable para almacenar el resultado de la comparación
      let isLiked = false;
  
      // Iterar a través de todas las claves almacenadas en el localStorage
      for (let key in localStorage) {
        // Verificar si la clave comienza con 'gustar_song_'
        if (key.startsWith('gustar_song_')) {
          // Obtener el ID de la canción desde la clave actual
          const storedId = getIdFromLocalStorageKey(key);
  
          // Comparar el ID almacenado con el ID que tienes en la variable
          if (storedId === id_song) {
            gustar_o_no = document.getElementById('song-saved')
            gustar_o_no.classList.add('saved')
            isLiked = true
            // Si encuentras una coincidencia, puedes detener el bucle si lo deseas.
            // break;
          }
        }
      }
  
      // Después de la iteración, puedes utilizar la variable isLiked para saber si el ID de la canción que tienes en la variable se encuentra en el localStorage.
      /*
      if (isLiked) {
        console.log('La canción con el ID ' + id_song + ' le gusta al usuario.');
      } else {
        console.log('La canción con el ID ' + id_song + ' NO le gusta al usuario.');
      }*/
  
  
  
  }, 5000);
}

/*
// Obtener el botón "Siguiente"
var nextButton = document.getElementById('next');

// Agregar un controlador de eventos para el evento "click"
nextButton.addEventListener('click', function() {
  getSongIdAfterDelay();

  // Avanzar a la siguiente canción utilizando la biblioteca AmplitudeJS
  document.getElementById('song-saved').classList.remove('saved')
});
*/
const xhr = new XMLHttpRequest();
xhr.open('GET', `${enviroments_url}/api/songs`);
let songs = [];

const promise = new Promise((resolve, reject) => {

  xhr.onload = () => {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.response);
      songs = data;
      resolve(songs);
    } else {
      reject('Error al realizar la solicitud');
    }
  };

  xhr.onerror = () => {
    reject('Error de red');
  };

});


 


promise.then((songs) => {
    Amplitude.init({
      "bindings": {
          /*37: 'prev',
          39: 'next',*/
          40: 'play_pause'
      },
      "callbacks": {
          timeupdate: function(){
              let percentage = Amplitude.getSongPlayedPercentage();

              if( isNaN( percentage ) ){
                  percentage = 0;
              }

              /**
               * Massive Help from: https://nikitahl.com/style-range-input-css
               */
              let slider = document.getElementById('song-percentage-played');
              slider.style.backgroundSize = percentage + '% 100%';
          }
      },
      "songs": songs
    });

    
    // aquí puedes hacer lo que quieras con los datos obtenidos
  }).catch((error) => {
    iziToast.error({
      title: 'Error',
      message: 'no se obtuvieron los datos correctamente',
    });
  });


xhr.send();



/*window.onkeydown = function(e) {
    return !(e.keyCode == 32);
};*/




//Mostrar Mensajes


let shownMessages = []; // arreglo para almacenar los ID de los mensajes que ya se han mostrado

// Función para obtener la lista de mensajes y mostrarlos en la página
function mostrarMensajes() {
  console.log("Enviando solicitud AJAX...");
  let xhr = new XMLHttpRequest();
  xhr.open('GET', `${enviroments_url}/chats`);
  
  xhr.onload = function() {
      if (xhr.status === 200) {
          let chatData = JSON.parse(xhr.responseText);
          // chatData ahora contiene los datos del archivo JSON como un objeto JavaScript
  
          // Crear elementos HTML para cada mensaje
          let messagesContainer = document.querySelector('.chat-messages');

          chatData.forEach(function(chat) {
              // Verificar si el mensaje ya se ha mostrado en la página

              // Buscar cualquier URL en el mensaje y convertirla en un enlace
              let urlRegex = /(https?:\/\/[^\s]+)/g;
              chat.message = chat.message.replace(urlRegex, '<a href="$&" target="_blank" style="color: red; font-weight: bold;">$&</a>');

              // Buscar todos los lenguajes de programación en la cadena de texto y resaltarlos en negrita con un color específico, excluyendo las URLs
              let languageRegex = /(?<![^\s])(?!https?:\/\/)(?:javascript|python|java|c#|c\+\+|php|django|node|rust|angular|laravel|go|kotlin|elixir|db|sql|ruby|next|good|projecto|linux|windows|vscode|nvim|vim|docker|tailwindcss)(?![^\s])/gi;
              chat.message = chat.message.replace(languageRegex, '<strong style="color: orange; font-weight: bold;">$&</strong>');
              

          

              if (!shownMessages.includes(chat.id)) {
                  let messageElement = document.createElement('div');
                  messageElement.classList.add('chat-message');
                  messageElement.classList.add('flex');
                  messageElement.classList.add('items-start');
                  messageElement.classList.add('mb-2');
                  messageElement.innerHTML = `
                  <div class="chat-messages px-4 py-2 overflow-y-auto flex-1 max-w-md break-words" id="chat-container" style="word-break: break-all;">
                  <div class="chat-message flex items-start mb-2">
                    <div class="chat-message-avatar mr-2">
                      <img src="${chat.avatar}" alt="Avatar" class="rounded-full object-cover avatar h-12" id="avatar" style="width:3rem;">
                    </div>
                    <div class="chat-message-content bg-gray-900  bg-opacity-80 rounded-lg px-3 py-2">
                      <div class="chat-message-username text-purple-600  font-bold">
                        <a href="account/profile/${chat.username}" target="_blank">${chat.username}</a>
                      </div>
                      <div class="chat-message-text text-gray-300 font-semibold message" id="message">
                            ${chat.message}
                      </div>
                    </div>
                  </div>
                </div>
  
                  `;
  
                  var userElement = document.getElementById('user-data');
                  var username = userElement.dataset.username;                  
                  if (chat.message.includes(`@${username}`)) {
                    
                    // Agregar un estilo especial al mensaje que menciona al usuario actual
                    messageElement.querySelector('.chat-message-content').style.border = '2px solid yellow';
                  }

                  var chatUsernames = document.querySelectorAll('.chat-message-username');
                  chatUsernames.forEach(function(chatUsername) {
                    var hue = Math.floor(Math.random() * 361); // generar valores de matiz de 0 a 360
                    var saturation = Math.floor(Math.random() * 31) + 60; // generar valores de saturación de 60 a 90
                    var brightness = Math.floor(Math.random() * 11) + 70; // generar valores de brillo de 70 a 80
                    var pastelColor = 'hsl(' + hue + ', ' + saturation + '%, ' + brightness + '%)';
                    chatUsername.style.color = pastelColor;
                  });


                  messagesContainer.appendChild(messageElement);
  
                  // Agregar el ID del mensaje al arreglo de mensajes mostrados
                  shownMessages.push(chat.id);
              }
          });
  
          // Función para hacer scroll hacia abajo
          const chatContainer = document.getElementById('chat-container');
          chatContainer.scrollTop = chatContainer.scrollHeight - chatContainer.clientHeight;
          var input = document.querySelector('.chat-input input');
          var message = input.value;

          // Hacer algo con los datos, por ejemplo:
      }
  };
  
  xhr.send();
}

// Enviar una solicitud AJAX cada 5 segundos para actualizar la lista de mensajes
setInterval(mostrarMensajes, 5000);


// Evento para el botón de enviar mensaje


document.querySelector('.chat-input button').addEventListener('click', function() {
  let input = document.querySelector('.chat-input input');
  let message = input.value;
  

  // Enviar el mensaje al servidor a través de una solicitud AJAX
  console.log("Enviando solicitud AJAX.. POSTTTT.");
  let xhr = new XMLHttpRequest();
  xhr.open('POST', `${enviroments_url}/chat/create`);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
      if (xhr.status === 200) {
          console.log("Mensaje enviado POSTTTT:", message);
          var response = JSON.parse(xhr.responseText);
          if (response.status === 'OK') {
              // Mostrar un mensaje de confirmación al usuario
              mostrarMensajes()
          } else {
              // Mostrar un mensaje de error al usuario
              iziToast.warning({
                position:'topLeft',
                title: 'Pendiente',
                message: response.message,
            });
          }
      }
  };
  xhr.send(JSON.stringify({message: message}));

  // Limpiar el campo de entrada y enfocarlo
  input.value = '';
  input.focus();

  /*
  const divElement = document.querySelector('.emojionearea-editor');

  // Vaciar el contenido del div cuando se haga clic en el botón
  
    divElement.textContent = '';*/
});

  // Agregar animación al mensaje al ingresar

// Escuchar el evento de envío de mensajes
