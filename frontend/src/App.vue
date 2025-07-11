<template>
    <div
      v-if="cargandoIA"
      class="fixed flex-col gap-4 inset-0 bg-black/60 flex items-center justify-center z-50"
    >
      <p class="text-white text-3xl">Esperando IA...</p>
      <div class="loader"></div>
    </div>
<!-- Botón SVG -->
<div
  class="block sm:hidden fixed right-0 p-4 rounded-bl-3xl bg-blue-800 z-50"
  @click="nueva()"
>
<svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 12H20M12 4V20" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
</div>

<div
  class="block sm:hidden fixed left-0 p-4 rounded-br-3xl bg-blue-800 z-50"
  @click="mostrarMenu = true"
>
  <svg class="size-6" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" fill="#ffffff">
    <!-- SVG content -->
    <circle cx="8" cy="24" r="6"></circle>
    <circle cx="24" cy="24" r="6"></circle>
    <circle cx="40" cy="24" r="6"></circle>
  </svg>
</div>

<!-- Capa negra -->
<div
  v-if="mostrarMenu"
  class="fixed inset-0 bg-black/60 z-40"
  @click="mostrarMenu = false"
></div>

<!-- Menú lateral derecho -->
<div
  v-if="mostrarMenu"
  class="fixed top-0 left-0 w-3/4 h-full bg-black z-50"
  @click.stop
>
<div
  v-for="nota in notasFiltradas"
  :key="nota.id"
  class="m-5 cursor-pointer group relative"
  @click="seleccionarNota(nota)"
>
  <!-- Botón sobrepuesto (solo aparece en hover) -->
  <div
    @click.stop="eliminar(nota)"
    class="absolute top-2 right-2 bg-fuchsia-700 text-white text-sm px-3 py-1 rounded-xl opacity-0 group-hover:opacity-100 transition duration-200"
  >
    <svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 6H20M16 6L15.7294 5.18807C15.4671 4.40125 15.3359 4.00784 15.0927 3.71698C14.8779 3.46013 14.6021 3.26132 14.2905 3.13878C13.9376 3 13.523 3 12.6936 3H11.3064C10.477 3 10.0624 3 9.70951 3.13878C9.39792 3.26132 9.12208 3.46013 8.90729 3.71698C8.66405 4.00784 8.53292 4.40125 8.27064 5.18807L8 6M18 6V16.2C18 17.8802 18 18.7202 17.673 19.362C17.3854 19.9265 16.9265 20.3854 16.362 20.673C15.7202 21 14.8802 21 13.2 21H10.8C9.11984 21 8.27976 21 7.63803 20.673C7.07354 20.3854 6.6146 19.9265 6.32698 19.362C6 18.7202 6 17.8802 6 16.2V6M14 10V17M10 10V17" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
      </div>

  <div class="p-4 hover:bg-fuchsia-900 transition border-b-2 border-amber-50">
    <div class="flex justify-between ">
      <p class="font-bold text-white text-lg">{{ nota.titulo }}</p>
      <p v-if="nota.ia" class="text-fuchsia-700">IA</p>
    </div>
    <p>
      {{ nota.descripcion.length > 100
        ? nota.descripcion.slice(0, 100) + '...'
        : nota.descripcion }}
    </p>
    <p class="mt-2 italic text-gray-400 line-clamp-2">{{ nota.ia }}</p>
  </div>
</div>
</div>

  <div class="min-h-screen bg-gray-950 text-white grid md:grid-cols-10">
    <div class="hidden md:block max-h-screen sm:col-span-1 md:col-span-5 xl:col-span-3 border-r-2 m-4 border-r-gray-800 overflow-y-auto scrollbar-thin scrollbar-thumb-fuchsia-600 scrollbar-track-gray-900">
        <p class="text-2xl mx-2">Ideas</p>
                <div class="flex gap-4 mx-5 h-10 mt-5">
          <div :disabled="!cargandoIA" @click="nueva()" class="flex justify-center items-center gap-4 bg-fuchsia-700   rounded-xl w-1/2">
          <p>Crear idea</p>
          <svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 12H20M12 4V20" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
        </div>
        <div :disabled="cargandoIA" v-if="!busqueda" @click="buscar()" class="flex justify-center items-center gap-4 bg-fuchsia-700   rounded-xl w-1/2">
          <p>Buscar idea</p>
          <svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M15.7955 15.8111L21 21M18 10.5C18 14.6421 14.6421 18 10.5 18C6.35786 18 3 14.6421 3 10.5C3 6.35786 6.35786 3 10.5 3C14.6421 3 18 6.35786 18 10.5Z" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
        </div>
        <div v-else @click="buscar()" class="flex justify-center items-center gap-4 bg-fuchsia-700   rounded-xl w-1/2">
          <p>Terminar busqueda</p>
          <svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M15.7955 15.8111L21 21M18 10.5C18 14.6421 14.6421 18 10.5 18C6.35786 18 3 14.6421 3 10.5C3 6.35786 6.35786 3 10.5 3C14.6421 3 18 6.35786 18 10.5Z" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
        </div>
        </div>
          <form @submit.prevent>
    <div v-if="busqueda" class="flex flex-col gap-4 m-5">
      <div>
        <label class="block text-sm mb-1">Título</label>
        <input v-model="filtros.titulo" class="border-2 border-fuchsia-700 p-2 w-full rounded-xl " type="text" />
      </div>

      <div>
        <label class="block text-sm mb-1">Descripción</label>
        <input v-model="filtros.descripcion" class="border-2 border-fuchsia-700 p-2 w-full rounded-xl " type="text" />
      </div>

      <div>
        <label class="block text-sm mb-1">IA</label>
        <input v-model="filtros.ia" class="border-2 border-fuchsia-700 p-2 w-full rounded-xl" type="text" />
      </div>

      <div class="h-30 overflow-y-auto scrollbar-thin scrollbar-thumb-fuchsia-600 scrollbar-track-gray-900">
        <label class="block text-sm mb-2">Etiquetas</label>
        <div class="grid grid-cols-2 md:grid-cols-3 flex-wrap">
          <div v-for="etiqueta in etiquetasUnicas" :key="etiqueta" class="flex items-center gap-2">
            <input
              type="checkbox"
              :value="etiqueta"
              v-model="filtros.etiquetasSeleccionadas"
              class="accent-fuchsia-700 mx-1"
            />
            <label>{{ etiqueta }}</label>
          </div>
        </div>
      </div>
    </div>
  </form>



<div
  v-for="nota in notasFiltradas"
  :key="nota.id"
  class="m-5 cursor-pointer group relative"
  @click="seleccionarNota(nota)"
>
  <!-- Botón sobrepuesto (solo aparece en hover) -->
  <div
    @click.stop="eliminar(nota)"
    class="absolute top-2 right-2 bg-fuchsia-700 text-white text-sm px-3 py-1 rounded-xl opacity-0 group-hover:opacity-100 transition duration-200"
  >
    <svg class="size-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 6H20M16 6L15.7294 5.18807C15.4671 4.40125 15.3359 4.00784 15.0927 3.71698C14.8779 3.46013 14.6021 3.26132 14.2905 3.13878C13.9376 3 13.523 3 12.6936 3H11.3064C10.477 3 10.0624 3 9.70951 3.13878C9.39792 3.26132 9.12208 3.46013 8.90729 3.71698C8.66405 4.00784 8.53292 4.40125 8.27064 5.18807L8 6M18 6V16.2C18 17.8802 18 18.7202 17.673 19.362C17.3854 19.9265 16.9265 20.3854 16.362 20.673C15.7202 21 14.8802 21 13.2 21H10.8C9.11984 21 8.27976 21 7.63803 20.673C7.07354 20.3854 6.6146 19.9265 6.32698 19.362C6 18.7202 6 17.8802 6 16.2V6M14 10V17M10 10V17" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
      </div>

  <div class="border p-4 rounded-xl hover:bg-fuchsia-900 transition">
    <div class="flex justify-between">
      <p class="font-bold text-lg">{{ nota.titulo }}</p>
      <p v-if="nota.ia" class="text-fuchsia-700">IA</p>
    </div>
    <p>
      {{ nota.descripcion.length > 100
        ? nota.descripcion.slice(0, 100) + '...'
        : nota.descripcion }}
    </p>
    <p class="mt-2 italic text-gray-400 line-clamp-2">{{ nota.ia }}</p>
    <div class="flex gap-4 mt-2">
      <p class="bg-fuchsia-700 px-2 rounded text-sm">{{ nota.etiqueta1 }}</p>
      <p class="bg-fuchsia-700 px-2 rounded text-sm">{{ nota.etiqueta2 }}</p>
      <p class="bg-fuchsia-700 px-2 rounded text-sm">{{ nota.etiqueta3 }}</p>
    </div>
  </div>
</div>

      </div>
    <div class="sm:col-span-9 md:col-span-5 xl:col-span-6">
      <div v-if="!notaSeleccionada" class="m-5">
        <p class="text-2xl sm:text-3xl mt-20 sm:mt-0">¿Tienes algo nuevo en mente?</p>
        <form class="mx-10 mt-10" @submit.prevent="guardarIdea">
          <div class="flex flex-col gap-4">
            <div>
              <p class="text-xl mb-2">Idea principal</p>
              <input
                v-model="titulo"
                @input="iniciarTemporizador"
                class="border-2 rounded-xl w-full h-15 p-2 border-fuchsia-600"
                type="text"
              />
            </div>
            <div>
              <p class="text-xl mb-2">Información adicional</p>
              <textarea
                v-model="descripcion"
                @input="iniciarTemporizador"
                class="border-2 rounded-xl w-full min-h-30 max-h-50 p-2 border-fuchsia-600"
              ></textarea>
            </div>

            <!-- Carga esqueleto o respuesta IA -->
            <div v-if="IA" class="bg-gray-900 rounded-2xl p-4 mt-4 shadow-lg border border-fuchsia-600">
              <!-- Skeleton loader -->
              <div v-if="cargandoIA" class="animate-pulse space-y-3">
                <div class="h-4 bg-gray-700 rounded w-1/3"></div>
                <div class="h-4 bg-gray-700 rounded w-5/6"></div>
                <div class="h-4 bg-gray-700 rounded w-4/6"></div>
                <div class="h-4 bg-gray-700 rounded w-3/4"></div>
              </div>

              <!-- Resultado IA -->
              <div v-else class="space-y-2">
                <p class="text-fuchsia-400 text-lg font-semibold">Información relacionada (IA)</p>
                <p class="text-white text-base whitespace-pre-line">{{ informacionRelacionada }}</p>
                <div @click="generarInformacionIA()" class="flex items-center gap-4 mt-6">
                    <p class="text-fuchsia-400 text-lg font-semibold">Volver a procesar</p>
                    <svg class="size-6" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill="#ffffff" d="M14.9547098,7.98576084 L15.0711,7.99552 C15.6179,8.07328 15.9981,8.57957 15.9204,9.12636 C15.6826,10.7983 14.9218,12.3522 13.747,13.5654 C12.5721,14.7785 11.0435,15.5888 9.37999,15.8801 C7.7165,16.1714 6.00349,15.9288 4.48631,15.187 C3.77335,14.8385 3.12082,14.3881 2.5472,13.8537 L1.70711,14.6938 C1.07714,15.3238 3.55271368e-15,14.8776 3.55271368e-15,13.9867 L3.55271368e-15,9.99998 L3.98673,9.99998 C4.87763,9.99998 5.3238,11.0771 4.69383,11.7071 L3.9626,12.4383 C4.38006,12.8181 4.85153,13.1394 5.36475,13.3903 C6.50264,13.9466 7.78739,14.1285 9.03501,13.9101 C10.2826,13.6916 11.4291,13.0839 12.3102,12.174 C13.1914,11.2641 13.762,10.0988 13.9403,8.84476 C14.0181,8.29798 14.5244,7.91776 15.0711,7.99552 L14.9547098,7.98576084 Z M11.5137,0.812976 C12.2279,1.16215 12.8814,1.61349 13.4558,2.14905 L14.2929,1.31193 C14.9229,0.681961 16,1.12813 16,2.01904 L16,6.00001 L12.019,6.00001 C11.1281,6.00001 10.6819,4.92287 11.3119,4.29291 L12.0404,3.56441 C11.6222,3.18346 11.1497,2.86125 10.6353,2.60973 C9.49736,2.05342 8.21261,1.87146 6.96499,2.08994 C5.71737,2.30841 4.57089,2.91611 3.68976,3.82599 C2.80862,4.73586 2.23802,5.90125 2.05969,7.15524 C1.98193,7.70202 1.47564,8.08224 0.928858,8.00448 C0.382075,7.92672 0.00185585,7.42043 0.0796146,6.87364 C0.31739,5.20166 1.07818,3.64782 2.25303,2.43465 C3.42788,1.22148 4.95652,0.411217 6.62001,0.119916 C8.2835,-0.171384 9.99651,0.0712178 11.5137,0.812976 Z"></path> </g></svg>
                </div>
              </div>
            </div>

            <!-- Toggle switch -->
            <div class="flex items-center mt-4 gap-3">
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="IA" class="sr-only peer">
                <div
                  class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-2 peer-focus:ring-fuchsia-500 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-fuchsia-600">
                </div>
              </label>
              <div class="flex justify-between gap-20">
                <div>
                  <span class="text-white text-lg select-none">Procesar con IA</span>
                </div>
              </div>
            </div>
            <button class="bg-fuchsia-700 p-3 rounded-2xl mt-4 text-xl">Guardar idea</button>
          </div>
        </form>
      </div>
      <div class="m-5" v-if="notaSeleccionada">
          <p class="text-3xl mt-20">Mira esta idea</p>
        <form class="mx-10 mt-10" @submit.prevent="guardarIdea">
          <div class="flex flex-col gap-4">
            <div>
              <p class="text-xl mb-2">Idea principal</p>
              <input
                v-model="notaSeleccionada.titulo"
                class="rounded-xl w-full h-15 p-2 border-fuchsia-600"
                type="text"
              />
            </div>
            <div v-if="notaSeleccionada.descripcion">
              <p class="text-xl mb-2">Información adicional</p>
              <textarea
                v-model="notaSeleccionada.descripcion"
                class="rounded-xl w-full min-h-30 max-h-50 p-2 border-fuchsia-600"
              ></textarea>
            </div>

            <!-- Carga esqueleto o respuesta IA -->
            <div v-if="IA" class="bg-gray-900 rounded-2xl p-4 mt-4 shadow-lg border border-fuchsia-600">
              <!-- Skeleton loader -->
              <div v-if="cargandoIA" class="animate-pulse space-y-3">
                <div class="h-4 bg-gray-700 rounded w-1/3"></div>
                <div class="h-4 bg-gray-700 rounded w-5/6"></div>
                <div class="h-4 bg-gray-700 rounded w-4/6"></div>
                <div class="h-4 bg-gray-700 rounded w-3/4"></div>
              </div>

              <!-- Resultado IA -->
              <div v-else class="space-y-2">
                <p class="text-fuchsia-400 text-lg font-semibold">Información relacionada (IA)</p>
                <p v-if="!informacionRelacionada" class="text-white text-base whitespace-pre-line">{{ notaSeleccionada.ia }}</p>
                <p v-else class="text-white text-base whitespace-pre-line">{{ informacionRelacionada }}</p>
                <div @click="modificarInformacionIA(notaSeleccionada)" class="flex items-center gap-4 mt-6">
                    <p class="text-fuchsia-400 text-lg font-semibold">Volver a procesar</p>
                    <svg class="size-6" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill="#ffffff" d="M14.9547098,7.98576084 L15.0711,7.99552 C15.6179,8.07328 15.9981,8.57957 15.9204,9.12636 C15.6826,10.7983 14.9218,12.3522 13.747,13.5654 C12.5721,14.7785 11.0435,15.5888 9.37999,15.8801 C7.7165,16.1714 6.00349,15.9288 4.48631,15.187 C3.77335,14.8385 3.12082,14.3881 2.5472,13.8537 L1.70711,14.6938 C1.07714,15.3238 3.55271368e-15,14.8776 3.55271368e-15,13.9867 L3.55271368e-15,9.99998 L3.98673,9.99998 C4.87763,9.99998 5.3238,11.0771 4.69383,11.7071 L3.9626,12.4383 C4.38006,12.8181 4.85153,13.1394 5.36475,13.3903 C6.50264,13.9466 7.78739,14.1285 9.03501,13.9101 C10.2826,13.6916 11.4291,13.0839 12.3102,12.174 C13.1914,11.2641 13.762,10.0988 13.9403,8.84476 C14.0181,8.29798 14.5244,7.91776 15.0711,7.99552 L14.9547098,7.98576084 Z M11.5137,0.812976 C12.2279,1.16215 12.8814,1.61349 13.4558,2.14905 L14.2929,1.31193 C14.9229,0.681961 16,1.12813 16,2.01904 L16,6.00001 L12.019,6.00001 C11.1281,6.00001 10.6819,4.92287 11.3119,4.29291 L12.0404,3.56441 C11.6222,3.18346 11.1497,2.86125 10.6353,2.60973 C9.49736,2.05342 8.21261,1.87146 6.96499,2.08994 C5.71737,2.30841 4.57089,2.91611 3.68976,3.82599 C2.80862,4.73586 2.23802,5.90125 2.05969,7.15524 C1.98193,7.70202 1.47564,8.08224 0.928858,8.00448 C0.382075,7.92672 0.00185585,7.42043 0.0796146,6.87364 C0.31739,5.20166 1.07818,3.64782 2.25303,2.43465 C3.42788,1.22148 4.95652,0.411217 6.62001,0.119916 C8.2835,-0.171384 9.99651,0.0712178 11.5137,0.812976 Z"></path> </g></svg>
                </div>
              </div>
            </div>

            <!-- Toggle switch -->
            <div class="flex items-center mt-4 gap-3">


            </div>
            <button class="bg-fuchsia-700 p-3 rounded-2xl mt-4 text-xl">Guardar idea</button>
          </div>
        </form>
      </div>


    </div>

    <div class="hidden h-full">
<div v-if="notaSeleccionada" class="flex gap-4 flex-col justify-center items-center h-full">
  <div class="flex justify-center items-center bg-fuchsia-900 w-full h-10 rounded-xl">
    <input v-model="notaSeleccionada.etiqueta1" class="text-center w-30" type="text" />
  </div>
  <div class="flex justify-center items-center bg-fuchsia-900 w-full h-10 rounded-xl">
    <input v-model="notaSeleccionada.etiqueta2" class="text-center w-30" type="text" />
  </div>
  <div class="flex justify-center items-center bg-fuchsia-900 w-full h-10 rounded-xl">
    <input v-model="notaSeleccionada.etiqueta3" class="text-center w-30" type="text" />
  </div>
</div>

    </div>
  </div>
</template>

<style>
/* Para navegadores basados en WebKit */
.scrollbar-thin::-webkit-scrollbar {
  width: 1px;
}

.scrollbar-thin::-webkit-scrollbar-track {
  background: #1a202c; /* gris oscuro */
}

.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #a855f7; /* fucsia (color fuchsia-600) */
  border-radius: 10px;
}


</style>


<script>
import axios from 'axios'

export default {
  data() {
    return {
      titulo: '',
      descripcion: '',
      informacionRelacionada: '',
      IA: true,
      cargandoIA: false, // Controla el skeleton
      hashtags: [],
      notas: [],
      mod: false,
      notaSeleccionada: null,
      busqueda: false,
      mostrarMenu: false,
      filtros: {
        titulo: '',
        descripcion: '',
        ia: '',
        etiquetasSeleccionadas: []
      },
      backendUrl: 'https://prueba-backend-zses.onrender.com'
    }
  },
  methods: {
    extraerHashtags(texto) {
      return texto.match(/#[\p{L}\p{N}_]+/gu) || []
    },
    async guardarIdea() {
      try {
        if (this.notaSeleccionada) {
          // Está editando una nota existente
          await this.actualizarNota()
        } else {
          // Está creando una nueva nota
          const res = await axios.post(`${this.backendUrl}/guardar_nota/`, {
            titulo: this.titulo,
            descripcion: this.descripcion,
            ia: this.informacionRelacionada,
            etiqueta1: this.hashtags[0] || '',
            etiqueta2: this.hashtags[1] || '',
            etiqueta3: this.hashtags[2] || ''
          })

          console.log('Respuesta:', res.data)
          alert('Idea guardada correctamente')
          this.titulo = ''
          this.descripcion = ''
          this.informacionRelacionada = ''
          this.hashtags = []
        }
      } catch (err) {
        console.error('Error al guardar idea:', err)
        alert('Error al guardar la idea')
      }
      this.cargarNotas()
    },
    async actualizarNota() {
      try {
        const nota = this.notaSeleccionada
        await axios.put(`${this.backendUrl}/editar_nota/${nota.id}`, {
          titulo: nota.titulo,
          descripcion: nota.descripcion,
          ia: this.informacionRelacionada || nota.ia,
          etiqueta1: nota.etiqueta1 || '',
          etiqueta2: nota.etiqueta2 || '',
          etiqueta3: nota.etiqueta3 || ''
        })

        alert('Nota actualizada correctamente')
        this.notaSeleccionada = null
        this.informacionRelacionada = ''
        this.cargarNotas()
      } catch (err) {
        console.error('Error al actualizar nota:', err)
        alert('Error al actualizar la nota')
      }
    },

    iniciarTemporizador() {
      if (this.temporizador) clearTimeout(this.temporizador)

      this.temporizador = setTimeout(() => {
        this.generarInformacionIA()
      }, 1000)
    },
    async cargarNotas() {
      try {
        const res = await axios.get(`${this.backendUrl}/notas/`)
        this.notas = res.data
      } catch (error) {
        console.error('Error al cargar notas:', error)
      }
    },
    nueva() {
      this.mod = true
      this.notaSeleccionada = null
      this.busqueda = null
    },
    buscar() {
      if (this.busqueda) {
        this.busqueda = false
        this.filtros = {
          titulo: '',
          descripcion: '',
          ia: '',
          etiquetasSeleccionadas: [],
        }
      } else {
        this.busqueda = true
        this.mod = null
      }
    },
    async eliminar(nota) {
      console.log('ID a eliminar:', nota.id)
      const confirmar = confirm(`¿Eliminar la idea "${nota.titulo}"?`)
      if (!confirmar) return

      try {
        await axios.delete(`${this.backendUrl}/eliminar_nota/${nota.id}`)
        this.cargarNotas()
        if (this.notaSeleccionada?.id === nota.id) {
          this.notaSeleccionada = null
        }
      } catch (error) {
        console.error('Error al eliminar la nota:', error)
        alert('No se pudo eliminar la idea.')
      }
    },

    seleccionarNota(nota) {
      this.notaSeleccionada = { ...nota } // clona para evitar mutar directamente
    },
    async generarInformacionIA() {
      if (!this.IA) return

      this.cargandoIA = true

      const mensaje = `Estás en una aplicación web que funciona como un diario inteligente. El siguiente texto es lo que ingresó el usuario. No hables como IA, no te presentes ni comentes lo que piensas.  
    Agrega información relevante que pueda interesarle al usuario.  
    No hagas preguntas al final, ya que el usuario no puede responderte.  
    Usa únicamente texto plano y retroalimenta el contenido.  
    No uses letras negritas, porque se ven los asteriscos  
    No agregues mucho texto, sé directo  
    Apoya al usuario en todo momento  
    Bríndale todo lo necesario en caso de verse confundido   
    También define la intención del usuario en 3 etiquetas para su fácil acceso, menciónalas al final con un hashtag como por ejemplo #metas  
    Estas 3 etiquetas escríbelas hasta el final, todo en minúsculas, sin espacios, palabras no muy rebuscadas y cortas, maximo 11 letras y si usas acentos usalos, no uses palabras en ingles
    Título: ${this.titulo}  
    Descripción: ${this.descripcion || "Ninguna"}`

      try {
        const res = await axios.post(`${this.backendUrl}/preguntar_gemini/`, {
          mensaje: mensaje
        })

        const respuesta = res.data.respuesta

        // Extraer hashtags
        this.hashtags = this.extraerHashtags(respuesta)

        // Eliminar hashtags del texto visible
        const textoSinHashtags = respuesta.replace(/#[\p{L}\p{N}_]+/gu, '').trim()

        // Guardar solo el texto limpio
        this.informacionRelacionada = textoSinHashtags

      } catch (err) {
        console.error('Error al generar información con IA:', err)
        this.informacionRelacionada = 'Ocurrió un error al procesar con IA.'
        this.hashtags = []
      } finally {
        this.cargandoIA = false
      }
    },
    async modificarInformacionIA(nota) {
      if (!this.IA) return

      this.cargandoIA = true

      const mensaje = `Estás en una aplicación web que funciona como un diario inteligente. El siguiente texto es lo que ingresó el usuario. No hables como IA, no te presentes ni comentes lo que piensas.  
    Agrega información relevante que pueda interesarle al usuario.  
    No hagas preguntas al final, ya que el usuario no puede responderte.  
    Usa únicamente texto plano y retroalimenta el contenido.  
    No uses letras negritas, porque se ven los asteriscos  
    No agregues mucho texto, sé directo  
    Apoya al usuario en todo momento  
    Bríndale todo lo necesario en caso de verse confundido   
    También define la intención del usuario en 3 etiquetas para su fácil acceso, menciónalas al final con un hashtag como por ejemplo #metas  
    Estas 3 etiquetas escríbelas hasta el final, todo en minúsculas, sin espacios, palabras no muy rebuscadas y cortas, maximo 11 letras y si usas acentos usalos, no uses palabras en ingles
    Previamente el usuario ya te habia pedido informacion la cual es esta  ${nota.ia}, para que no la repitas
    Si el usuario deja todo en blanco dale ideas de que puede empezar
    Título: ${nota.titulo}  
    Descripción: ${nota.descripcion || "Ninguna"}`

      try {
        const res = await axios.post(`${this.backendUrl}/preguntar_gemini/`, {
          mensaje: mensaje
        })

        const respuesta = res.data.respuesta

        // Extraer hashtags
        this.hashtags = this.extraerHashtags(respuesta)

        // Eliminar hashtags del texto visible
        const textoSinHashtags = respuesta.replace(/#[\p{L}\p{N}_]+/gu, '').trim()

        // Guardar solo el texto limpio
        this.informacionRelacionada = textoSinHashtags

      } catch (err) {
        console.error('Error al generar información con IA:', err)
        this.informacionRelacionada = 'Ocurrió un error al procesar con IA.'
        this.hashtags = []
      } finally {
        this.cargandoIA = false
      }
    }
  },
  mounted() {
    this.cargarNotas()
  },
  computed: {
    notasFiltradas() {
      return this.notas.filter(nota => {
        const coincideTitulo = nota.titulo.toLowerCase().includes(this.filtros.titulo.toLowerCase())
        const coincideDescripcion = nota.descripcion.toLowerCase().includes(this.filtros.descripcion.toLowerCase())
        const coincideIA = (nota.ia || '').toLowerCase().includes(this.filtros.ia.toLowerCase())

        const etiquetasNota = [nota.etiqueta1, nota.etiqueta2, nota.etiqueta3]
          .filter(Boolean)
          .map(e => e.toLowerCase())

        const etiquetasSeleccionadas = this.filtros.etiquetasSeleccionadas.map(e => e.toLowerCase())

        const coincideEtiquetas = etiquetasSeleccionadas.every(e => etiquetasNota.includes(e))

        return coincideTitulo && coincideDescripcion && coincideIA && coincideEtiquetas
      })
    },
    etiquetasUnicas() {
      const etiquetas = new Set()
      this.notas.forEach(nota => {
        if (nota.etiqueta1) etiquetas.add(nota.etiqueta1)
        if (nota.etiqueta2) etiquetas.add(nota.etiqueta2)
        if (nota.etiqueta3) etiquetas.add(nota.etiqueta3)
      })
      return Array.from(etiquetas)
    }
  }
}
</script>
<style scoped>
/* Loader CSS simple: spinner */
.loader {
  border: 8px solid #f3f3f3; /* Light grey */
  border-top: 8px solid #a855f7; /* Fuchsia purple */
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
