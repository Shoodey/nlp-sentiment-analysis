<template>
    <div class="content-wrapper">
        <section class="content-header">
            <h1>
                Dashboard
                <small>A general overview</small>
            </h1>
            <ol class="breadcrumb">
                <li><a href="javascript:void(0)"><i class="fa fa-dashboard"></i> Dashboard</a></li>
            </ol>
        </section>

        <section class="content">
            <div class="row">
                <div class="col-md-3">
                    <div class="small-box bg-aqua">
                        <div class="inner">
                            <h3>Twitter</h3>
                            <p>&nbsp;</p>
                        </div>
                        <div class="icon">
                            <i class="fa fa-twitter"></i>
                        </div>
                            <router-link :to="'/twitter'" :class="'small-box-footer'">
                                View analysis <i class="fa fa-arrow-circle-right"></i>
                            </router-link>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="small-box bg-orange">
                        <div class="inner">
                            <h3>IMDb</h3>
                            <p>&nbsp;</p>
                        </div>
                        <div class="icon">
                            <i class="fa fa-imdb"></i>
                        </div>
                            <router-link :to="'/imdb'" :class="'small-box-footer'">
                                View analysis <i class="fa fa-arrow-circle-right"></i>
                            </router-link>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>

    export default {

        data() {
            return {

            }
        },

        mounted() {
            $('html, body, .wrapper').css('height', '100%');
        }
    }
</script>