<template>
  <div>
    <h1>Helpful Information</h1>
    <br>
	<input type="text" placeholder="Enter key word" id="find" autofocus ="on" style="font-weight:bold;">     
	<div id="find">
    <button v-on:click="search()">Поиск</button>
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
    console.log("This function is for searching info")
    },
  },
  layout: "main"
  };
</script>

  <style>
   #find {
    width: 300px; /* Ширина поля в пикселах */
   } 
  </style>
