# Learning Blocks Vue.js Front End

## 1. How to set up a router

> This section talks about adding a new route in your Vue project. 

1. Create an empty page
```
<template>
    <p>Sample Page</p>
</template>
```
2. Add the new view to the router object
> This can be found in the index.js file located in the "src/router" folder
```
import { createRouter, createWebHistory } from  'vue-router'
import  HomeView  from  '../views/HomeView.vue'

const  router  =  createRouter({

	history:  createWebHistory(import.meta.env.BASE_URL),

	routes: [

		{

			path:  '/',

			name:  'home',

			component: HomeView

		},
		// Import all other routes as such to lazy-load only when visited
		// {
		//     path: '/sample-path',
		//     name: 'sample',
		//     component: () => import('../views/ViewFile.vue')
		// }
	]
})

export  default  router
```

3.  (Optional) Add RouterLink elements to create anchors
```
// In your desired page/component

<RouterLink  to="/sample-link">Sample View</RouterLink>
```


