import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Projects from '@/components/Projects'
import Grid1 from '@/components/Grid1'
import FullpageTest from '@/components/FullpageTest'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/projects',
      name: 'Projects',
      component: Projects
    },
    {
      path: '/grid1',
      name: 'Grid1',
      component: Grid1
    },
    {
      path: '/fullpagetest',
      name: 'FullpageTest',
      component: FullpageTest
    }
  ]
})
