<template>
  <div class="w-full ml-28">
    <div class="font-bold text-xl tracking-wide mt-2 mb-2 text-left">
      Reviews
    </div>
    <!-- Первый отзыв + блок модерации -->
    <div class="flex justify-start">
      <div
        class="rounded-lg divide-purple-300 border-solid border-2 border-purple-200 w-1/2"
      >
        <div class="flex items-start">
          <div class="flex-shrink-0">
            <div class="my-3 mx-3 inline-block relative">
              <div class="relative w-16 h-16 rounded-full overflow-hidden">
                <img
                  class="absolute top-0 left-0 w-full h-full bg-cover object-fit object-cover"
                  src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                  alt="Profile picture"
                />
                <div
                  class="absolute top-0 left-0 w-full h-full rounded-full shadow-inner"
                ></div>
              </div>
              <svg
                class="fill-current text-white bg-green-600 rounded-full p-1 absolute bottom-0 right-0 w-6 h-6 -mx-1 -my-1"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M19 11a7.5 7.5 0 0 1-3.5 5.94L10 20l-5.5-3.06A7.5 7.5 0 0 1 1 11V3c3.38 0 6.5-1.12 9-3 2.5 1.89 5.62 3 9 3v8zm-9 1.08l2.92 2.04-1.03-3.41 2.84-2.15-3.56-.08L10 5.12 8.83 8.48l-3.56.08L8.1 10.7l-1.03 3.4L10 12.09z"
                />
              </svg>
            </div>
          </div>
          <div class="mx-6 mt-4">
            <p class="flex items-baseline">
              <span class="text-gray-600 font-bold">Jane C.</span>
              <span class="ml-2 text-green-600 text-xs">Verified Client</span>
            </p>
            <div class="flex items-center mt-1">
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
            </div>
            <div class="flex items-center mt-4 text-gray-600">
              <div class="flex items-center">
                <span class="text-sm">Quality</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-sm">Experience</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <div class="mt-3">
              <span class="font-bold">Tips for future users!</span>
              <p class="mt-1">
                This service is of very good quality, not expensive, the cars
                are in proper condition! Thanks!
              </p>
            </div>
            <div
              class="flex items-center justify-between mt-4 text-sm text-gray-600 fill-current"
            >
              <button class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                  />
                </svg>
                <span class="ml-2">Add to favorites</span>
              </button>
              <div class="flex items-center">
                <span class="text-purple-500 underline"
                  >Was this review helplful?</span
                >
                <button class="flex items-center ml-6">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 0h1v3l3 7v8a2 2 0 0 1-2 2H5c-1.1 0-2.31-.84-2.7-1.88L0 12v-2a2 2 0 0 1 2-2h7V2a2 2 0 0 1 2-2zm6 10h3v10h-3V10z"
                    />
                  </svg>
                  <span class="ml-2">56</span>
                </button>
                <button class="flex items-center ml-4">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 20a2 2 0 0 1-2-2v-6H2a2 2 0 0 1-2-2V8l2.3-6.12A3.11 3.11 0 0 1 5 0h8a2 2 0 0 1 2 2v8l-3 7v3h-1zm6-10V0h3v10h-3z"
                    />
                  </svg>
                  <span class="ml-2">2</span>
                </button>
              </div>
            </div>
            <div class="mt-5">
              <textarea
                class="w-full py-2 px-2 mt-1 border-solid border-2 rounded-lg border-purple-100"
                name=""
                id=""
                placeholder="Send a comment for this review"
                rows="5"
              ></textarea>
              <div class="w-full flex justify-end">
                <div class="mr-2">
                  <a
                    class="tracking-wider uppercase font-bold text-green-700 hover:bg-green-100 rounded p-2 inline-block"
                    href="#"
                    >SEND</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="mx-5 w-1/3">
        <div
          class="sm:rounded-lg material-card bg-white border-solid border-2 border-purple-200"
        >
          <div class="px-6 py-4">
            <div class="flex justify-start mb-5">
              <div class="relative w-16 h-16 rounded-full overflow-hidden">
                <img
                  class="absolute top-0 left-0 w-full h-full bg-cover object-fit object-cover"
                  src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                  alt="Profile picture"
                />
                <div
                  class="absolute top-0 left-0 w-full h-full rounded-full shadow-inner"
                ></div>
              </div>
              <div>
                <div class="font-bold text-xl ml-2 mt-2 tracking-wide">
                  Jane Cooper
                </div>
                <span class="ml-2 text-green-600 text-xs">Verified Client</span>
              </div>
            </div>
            <div class="">
              <div class="flex items-center">
                <span class="text-sm">Quality</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
              <div class="flex items-center">
                <span class="text-sm">Experience</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <p class="mt-4">Title:</p>
            <div class="flex justify-start mt-3">
              <input
                class="font-bold w-full py-2 px-2 border-solid border-2 rounded-lg border-purple-100"
                value="Tips for future users!"
              />
            </div>
            <p class="mt-4 mr-3">Body:</p>
            <textarea
              class="w-full py-2 px-2 mt-1 border-solid border-2 rounded-lg border-purple-100"
            >
This service is of very good quality, not expensive, the cars are in proper condition! Thanks!</textarea
            >
            <div class="mt-2 w-full flex justify-end">
              <a
                class="tracking-wider uppercase font-bold text-red-700 hover:bg-red-100 rounded p-2 inline-block"
                href="#"
                >DELETE</a
              >
              <a
                class="tracking-wider uppercase font-bold text-green-700 hover:bg-green-100 rounded p-2 inline-block"
                href="#"
                >ATTACH</a
              >
              <a
                class="mr-2 tracking-wider uppercase font-bold text-purple-700 hover:bg-purple-100 rounded p-2 inline-block"
                href="#"
                >UPDATE</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Остальные отзывы -->
    <div>
      <div
        class="my-4 rounded-lg divide-purple-300 border-solid border-2 border-purple-200 w-1/2"
      >
        <div class="flex items-start">
          <div class="flex-shrink-0">
            <div class="my-3 mx-3 inline-block relative">
              <div class="relative w-16 h-16 rounded-full overflow-hidden">
                <img
                  class="absolute top-2 left-0 w-full h-full bg-cover object-fit object-cover"
                  src="~/static/img/free-icon-student-4472500.png"
                  alt="Profile picture"
                />
                <div
                  class="absolute top-0 left-0 w-full h-full rounded-full shadow-inner"
                ></div>
              </div>
              <svg
                class="fill-current text-white bg-green-600 rounded-full p-1 absolute bottom-0 right-0 w-6 h-6 -mx-1 -my-1"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M19 11a7.5 7.5 0 0 1-3.5 5.94L10 20l-5.5-3.06A7.5 7.5 0 0 1 1 11V3c3.38 0 6.5-1.12 9-3 2.5 1.89 5.62 3 9 3v8zm-9 1.08l2.92 2.04-1.03-3.41 2.84-2.15-3.56-.08L10 5.12 8.83 8.48l-3.56.08L8.1 10.7l-1.03 3.4L10 12.09z"
                />
              </svg>
            </div>
          </div>
          <div class="mx-6 my-4 pb-3">
            <p class="flex items-baseline">
              <span class="text-gray-600 font-bold">Brown Green</span>
              <span class="ml-2 text-green-600 text-xs">Verified Client</span>
            </p>
            <div class="flex items-center mt-1">
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
            </div>
            <div class="flex items-center mt-4 text-gray-600">
              <div class="flex items-center">
                <span class="text-sm">Quality</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-sm">Experience</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <div class="mt-3">
              <span class="font-bold">~</span>
              <p class="mt-1">
                Amazing service! I have been using it for the second year. Thank
                you so much, guys.
              </p>
            </div>
            <div
              class="flex items-center justify-between mt-4 text-sm text-gray-600 fill-current"
            >
              <button class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                  />
                </svg>
                <span class="ml-2">Add to favorites</span>
              </button>
              <div class="flex items-center">
                <span class="text-purple-500 underline"
                  >Was this review helplful?</span
                >
                <button class="flex items-center ml-6">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 0h1v3l3 7v8a2 2 0 0 1-2 2H5c-1.1 0-2.31-.84-2.7-1.88L0 12v-2a2 2 0 0 1 2-2h7V2a2 2 0 0 1 2-2zm6 10h3v10h-3V10z"
                    />
                  </svg>
                  <span class="ml-2">7</span>
                </button>
                <button class="flex items-center ml-4">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 20a2 2 0 0 1-2-2v-6H2a2 2 0 0 1-2-2V8l2.3-6.12A3.11 3.11 0 0 1 5 0h8a2 2 0 0 1 2 2v8l-3 7v3h-1zm6-10V0h3v10h-3z"
                    />
                  </svg>
                  <span class="ml-2">0</span>
                </button>
              </div>
            </div>
            <!-- <div class="mt-5">
              <textarea
                class="w-full py-2 px-2 mt-1 border-solid border-2 rounded-lg border-purple-100"
                name=""
                id=""
                placeholder="Send a comment for this review"
                rows="6"
              ></textarea>
              <div class="w-full flex justify-end">
                <div class="mr-2">
                  <a
                    class="tracking-wider uppercase font-bold text-green-700 hover:bg-green-100 rounded p-2 inline-block"
                    href="#"
                    >SEND</a
                  >
                </div>
              </div>
            </div> -->
          </div>
        </div>
      </div>
      <div
        class="my-4 rounded-lg divide-purple-300 border-solid border-2 border-purple-200 w-1/2"
      >
        <div class="flex items-start">
          <div class="flex-shrink-0">
            <div class="my-3 mx-3 inline-block relative">
              <div class="relative w-16 h-16 rounded-full overflow-hidden">
                <img
                  class="absolute top-1 left-0 w-full h-full bg-cover object-fit object-cover"
                  src="~/static/img/free-icon-teenager-4472485.png"
                  alt="Profile picture"
                />
                <div
                  class="absolute top-0 left-0 w-full h-full rounded-full shadow-inner"
                ></div>
              </div>
              <svg
                class="fill-current text-white bg-red-600 rounded-full p-1 absolute bottom-0 right-0 w-6 h-6 -mx-1 -my-1"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M19 11a7.5 7.5 0 0 1-3.5 5.94L10 20l-5.5-3.06A7.5 7.5 0 0 1 1 11V3c3.38 0 6.5-1.12 9-3 2.5 1.89 5.62 3 9 3v8zm-9 1.08l2.92 2.04-1.03-3.41 2.84-2.15-3.56-.08L10 5.12 8.83 8.48l-3.56.08L8.1 10.7l-1.03 3.4L10 12.09z"
                />
              </svg>
            </div>
          </div>
          <div class="mx-6 my-4 pb-3">
            <p class="flex items-baseline">
              <span class="text-gray-600 font-bold">Anonymous</span>
              <span class="ml-2 text-red-600 text-xs">Not Verified</span>
            </p>
            <div class="flex items-center mt-1">
              <svg
                class="w-4 h-4 fill-current text-yellow-600"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
              <svg
                class="w-4 h-4 fill-current text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                />
              </svg>
            </div>
            <div class="flex items-center mt-4 text-gray-600">
              <div class="flex items-center">
                <span class="text-sm">Quality</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-sm">Experience</span>
                <div class="flex items-center ml-2">
                  <svg
                    class="w-3 h-3 fill-current text-yellow-600"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                  <svg
                    class="w-3 h-3 fill-current text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <div class="mt-3">
              <span class="font-bold">~</span>
              <p class="mt-1 text-gray-500">
                That review was removed. Because it violates the rules of the
                service.
              </p>
            </div>
            <div
              class="flex items-center justify-between mt-4 text-sm text-gray-600 fill-current"
            >
              <button class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                  />
                </svg>
                <span class="ml-2">Add to favorites</span>
              </button>
              <div class="flex items-center">
                <span class="text-purple-500 underline"
                  >Was this review helplful?</span
                >
                <button class="flex items-center ml-6">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 0h1v3l3 7v8a2 2 0 0 1-2 2H5c-1.1 0-2.31-.84-2.7-1.88L0 12v-2a2 2 0 0 1 2-2h7V2a2 2 0 0 1 2-2zm6 10h3v10h-3V10z"
                    />
                  </svg>
                  <span class="ml-2">0</span>
                </button>
                <button class="flex items-center ml-4">
                  <svg
                    class="w-3 h-3"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M11 20a2 2 0 0 1-2-2v-6H2a2 2 0 0 1-2-2V8l2.3-6.12A3.11 3.11 0 0 1 5 0h8a2 2 0 0 1 2 2v8l-3 7v3h-1zm6-10V0h3v10h-3z"
                    />
                  </svg>
                  <span class="ml-2">0</span>
                </button>
              </div>
            </div>
            <!-- <div class="mt-5">
              <textarea
                class="w-full py-2 px-2 mt-1 border-solid border-2 rounded-lg border-purple-100"
                name=""
                id=""
                placeholder="Send a comment for this review"
                rows="6"
              ></textarea>
              <div class="w-full flex justify-end">
                <div class="mr-2">
                  <a
                    class="tracking-wider uppercase font-bold text-green-700 hover:bg-green-100 rounded p-2 inline-block"
                    href="#"
                    >SEND</a
                  >
                </div>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    startdate: "",
    clockStart: null,
    timeOnPage: null,
    tempSecs: 0,
  }),

  created() {},

  methods: {
    search() {
      console.log("This function is for searching info");
    },
  },
  layout: "main",
};
</script>

<style>
#find {
  width: 300px; /* Ширина поля в пикселах */
}
</style>
