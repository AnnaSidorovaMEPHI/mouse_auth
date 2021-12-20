<template>
  <div id="app">
  <h2>Storage</h2>
  <div v-for="(obj,n) in objs">
    <p>
    <span class="obj">{{obj}}</span> <button @click="removeObj(n)">Remove</button>
    </p>
  </div>
  
  <p>
    <input v-model="newObj"> 
    <button @click="addObj">Add Object</button>
  </p>
  
</div>
</template>



<script>
export default {
  
  data: () => ({
    objs: [],
    newObj: null
  }),
  mounted() {
    if (localStorage.getItem('objs')) {
      try {
        this.objs = JSON.parse(localStorage.getItem('objs'));
      } catch(e) {
        localStorage.removeItem('objs');
      }
    }
  },
  methods: {
    addObj() {
      // убедиться, что было что-либо введено
      if (!this.newObj) {
        return;
      }

      this.objs.push(this.newObj);
      this.newObj = '';
      this.saveObjs();
    },
    removeObj(x) {
      this.objs.splice(x, 1);
      this.saveObjs();
    },
    saveObjs() {
      const parsed = JSON.stringify(this.objs);
      localStorage.setItem('objs', parsed);
    }
  },

  head() {
    return {
      title: "",
      meta: [{ hid: "description", name: "description", content: "Test desc" }]
    };
  }
};
</script>


