<template>
    <header class="main-header">
        <router-link :to="'/'" class="logo">
            <span class="logo-mini"><b>NLP</b></span>
            <span class="logo-lg">Sentiment Analysis</span>
        </router-link>

        <nav class="navbar navbar-static-top">
            <a href="javascript:void(0)" class="sidebar-toggle" data-toggle="push-menu" role="button">
                <span class="sr-only">Toggle navigation</span>
            </a>
            <div class="navbar-custom-menu">
                <ul class="nav navbar-nav">
                    <li class="dropdown messages-menu">
                        <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="fa fa-envelope-o"></i>
                            <span class="label label-success">{{ unreadMessagesCount }}</span>
                        </a>
                        <ul class="dropdown-menu">
                            <li class="header">You have {{ unreadMessagesCount }} messages</li>
                            <li>
                                <ul class="menu">
                                    <li>
                                        <a href="javascript:void(0)">
                                            <div class="pull-left">
                                                <img src="~admin-lte/dist/img/user3-128x128.jpg" class="img-circle"
                                                     alt="User Image">
                                            </div>
                                            <h4>
                                                Jane
                                                <small><i class="fa fa-clock-o"></i> 2 hours</small>
                                            </h4>
                                            <p>Lorem ipsum dolor sit.</p>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="javascript:void(0)">
                                            <div class="pull-left">
                                                <img src="~admin-lte/dist/img/user4-128x128.jpg" class="img-circle"
                                                     alt="User Image">
                                            </div>
                                            <h4>
                                                Karla
                                                <small><i class="fa fa-clock-o"></i> Today</small>
                                            </h4>
                                            <p>Lorem ipsum dolor sit.</p>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                            <li class="footer"><a href="javascript:void(0)">See All Messages</a></li>
                        </ul>
                    </li>

                    <li class="dropdown notifications-menu">
                        <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="fa fa-bell-o"></i>
                            <span class="label label-warning">{{ unreadNotificationsCount }}</span>
                        </a>
                        <ul class="dropdown-menu">
                            <li class="header">You have {{ unreadNotificationsCount }} notifications</li>
                            <li>
                                <ul class="menu">
                                    <li>
                                        <a href="javascript:void(0)">
                                            <i class="fa fa-warning text-yellow"></i>
                                            Lorem ipsum dolor sit.
                                        </a>
                                    </li>
                                    <li>
                                        <a href="javascript:void(0)">
                                            <i class="fa fa-users text-red"></i>
                                            Lorem ipsum dolor sit.
                                        </a>
                                    </li>
                                </ul>
                            </li>
                            <li class="footer"><a href="javascript:void(0)">View all</a></li>
                        </ul>
                    </li>
                    <li class="dropdown tasks-menu">
                        <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="fa fa-flag-o"></i>
                            <span class="label label-danger">{{ remainTasksCount }}</span>
                        </a>
                        <ul class="dropdown-menu">
                            <li class="header">You have {{ remainTasksCount }} tasks</li>
                            <li>
                                <ul class="menu">
                                    <li>
                                        <a href="javascript:void(0)">
                                            <h3>
                                                Lorem ipsum dolor sit.
                                                <small class="pull-right">80%</small>
                                            </h3>
                                            <div class="progress xs">
                                                <div class="progress-bar progress-bar-green" style="width: 80%"
                                                     role="progressbar" aria-valuenow="20" aria-valuemin="0"
                                                     aria-valuemax="100">
                                                    <span class="sr-only">80% Complete</span>
                                                </div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="javascript:void(0)">
                                            <h3>
                                                Lorem ipsum dolor sit.
                                                <small class="pull-right">20%</small>
                                            </h3>
                                            <div class="progress xs">
                                                <div class="progress-bar progress-bar-red" style="width: 20%"
                                                     role="progressbar" aria-valuenow="20" aria-valuemin="0"
                                                     aria-valuemax="100">
                                                    <span class="sr-only">20% Complete</span>
                                                </div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="javascript:void(0)">
                                            <h3>
                                                Lorem ipsum dolor sit.
                                                <small class="pull-right">60%</small>
                                            </h3>
                                            <div class="progress xs">
                                                <div class="progress-bar progress-bar-yellow" style="width: 60%"
                                                     role="progressbar" aria-valuenow="20" aria-valuemin="0"
                                                     aria-valuemax="100">
                                                    <span class="sr-only">60% Complete</span>
                                                </div>
                                            </div>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                            <li class="footer">
                                <a href="javascript:void(0)">View all tasks</a>
                            </li>
                        </ul>
                    </li>
                    <!-- User Account: style can be found in dropdown.less -->
                    <li class="dropdown user user-menu">
                        <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown">
                            <img src="~admin-lte/dist/img/user2-160x160.jpg" class="user-image" alt="User Image">
                            <span class="hidden-xs">{{ currentUser.name }}</span>
                        </a>
                        <ul class="dropdown-menu">
                            <!-- User image -->
                            <li class="user-header">
                                <img src="~admin-lte/dist/img/user2-160x160.jpg" class="img-circle" alt="User Image">

                                <p>
                                    {{ currentUser.name }}
                                     <!-- - {{ currentUser.position }}-->
                                    <small>Registered since {{ currentUser.createdAt }}</small>
                                </p>
                            </li>
                            <!-- Menu Body -->
                            <!--<li class="user-body">-->
                            <!--<div class="row">-->
                            <!--<div class="col-xs-4 text-center">-->
                            <!--<a href="javascript:void(0)">Followers</a>-->
                            <!--</div>-->
                            <!--<div class="col-xs-4 text-center">-->
                            <!--<a href="javascript:void(0)">Sales</a>-->
                            <!--</div>-->
                            <!--<div class="col-xs-4 text-center">-->
                            <!--<a href="javascript:void(0)">Friends</a>-->
                            <!--</div>-->
                            <!--</div>-->
                            <!--</li>-->
                            <!-- Menu Footer-->
                            <li class="user-footer">
                                <!--<div class="pull-left">-->
                                    <!--<a href="javascript:void(0)" class="btn btn-default btn-flat">Shows</a>-->
                                <!--</div>-->
                                <div class="pull-right">
                                    <a href="javascript:void(0)" class="btn btn-default btn-flat">Sign out</a>
                                </div>
                            </li>
                        </ul>
                    </li>
                    <!-- Control Sidebar Toggle Button -->
                    <!--<li>-->
                        <!--<a href="javascript:void(0)" data-toggle="control-sidebar"><i class="fa fa-gears"></i></a>-->
                    <!--</li>-->
                </ul>
            </div>
        </nav>
    </header>
</template>

<script>
    import moment from 'moment'

    export default {
        name: 'Topbar',

        data() {
            return {
                unreadMessagesCount: 2,
                unreadNotificationsCount: 2,
                remainTasksCount: 3,
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