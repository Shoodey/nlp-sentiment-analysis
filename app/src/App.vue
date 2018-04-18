<template>
    <div id="app" class="wrapper">
        <topbar></topbar>
        <sidebar></sidebar>
        <router-view></router-view>
        <footer class="main-footer">
            Made with <i class="fa fa-heart" style="color: #ff4e5f"></i> and <span class="fa fa-coffee" style="color: #805f40"></span> by
            <a href="shoodey.me">EL AMRI Ali</a>.
        </footer>
    </div>
</template>

<script>
    import Topbar from '@/components/Topbar'
    import Sidebar from '@/components/Sidebar'

    export default {
        name: 'App',
        components: {Topbar, Sidebar}
    }
</script>
