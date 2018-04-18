import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Twitter from '@/components/Twitter'
import IMDb from '@/components/IMDb'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Dashboard',
            component: Dashboard
        },
        {
            path: '/twitter',
            name: 'Twitter',
            component: Twitter
        },
        {
            path: '/imdb',
            name: 'IMDb',
            component: IMDb
        }
    ]
})
