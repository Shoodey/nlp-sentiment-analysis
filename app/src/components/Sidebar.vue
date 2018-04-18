<template>
    <aside id="slider" class="main-sidebar">
        <section class="sidebar">
            <div class="user-panel">
                <div class="pull-left image">
                    <img src="~admin-lte/dist/img/user2-160x160.jpg" class="img-circle" alt="User Image">
                </div>
                <div class="pull-left info">
                    <p>{{ currentUser.name }}</p>
                    <a href="javascript:void(0)"><i class="fa fa-circle"
                                                    :style="`color:${currentUser.state.color}`"></i> {{
                        currentUser.state.name }}</a>
                </div>
            </div>

            <ul class="sidebar-menu tree" data-widget="tree">
                <li class="header">Sentiment Analysis</li>
                <li class="active">
                    <router-link :to="'/'">
                        <i class="fa fa-th"></i>
                        <span>Dashboard</span>
                    </router-link>
                </li>
            </ul>
        </section>
    </aside>
</template>

<script>
    import moment from 'moment'

    export default {
        name: 'Sidebar',

        data() {
            return {
                currentUser: {
                    name: 'John DOE',
                    position: 'Show Designer',
                    state: {
                        color: '#3c763d',
                        name: 'Online'
                    },
                    createdAt: moment().format("MMMM Do YYYY")
                },
            }
        }
    }
</script>