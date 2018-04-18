<template>
    <div class="content-wrapper">
        <section class="content-header" v-if="!category && !videos && !video">
            <h1>
                Twitter Corpus
                <small>Video Categories</small>
            </h1>
            <ol class="breadcrumb">
                <li><router-link :to="'/'">
                    <i class="fa fa-th"></i> Dashboard
                </router-link></li>
                <li class="active">Twitter</li>
            </ol>
        </section>

        <section class="content-header" v-if="category && videos && !video">
            <h1>
                {{ category }} Video
                <small>Videos List (Twitter Corpus)</small>
            </h1>
            <ol class="breadcrumb">
                <li><router-link :to="'/'">
                    <i class="fa fa-th"></i> Dashboard
                </router-link></li>
                <li><a href="javascript:void(0)" @click="() => {category = null; videos = null, video = null}">
                    Twitter
                </a></li>
                <li class="active">Videos List</li>
            </ol>
        </section>

        <section class="content-header" v-if="video">
            <h1>
                {{ video.title }}
                <small>Video details (Twitter Corpus)</small>
            </h1>
            <ol class="breadcrumb">
                <li><router-link :to="'/'">
                    <i class="fa fa-th"></i> Dashboard
                </router-link></li>
                <li><a href="javascript:void(0)" @click="() => {category = null; videos = null, video = null}">
                    Twitter
                </a></li>
                <li><a href="javascript:void(0)" @click="() => {video = null}">
                    {{ category }} videos
                </a></li>
                <li class="active">Video details</li>
            </ol>
        </section>

        <section class="content">
           <div class="row" v-if="!video">
               <div class="col-md-4">
                   <div class="box box-widget widget-user">
                       <div class="widget-user-header bg-aqua-active">
                           <h3 class="widget-user-username">Automobiles</h3>
                           <h5 class="widget-user-desc">Fast & Furious</h5>
                       </div>
                       <div class="widget-user-image">
                           <a href="javascript:void(0)" @click="() => {category = 'Autos'; videos = autoVideos}">
                               <img class="img-circle" src="@/assets/car.jpg" style="max-width: 90px">
                           </a>
                       </div>
                       <div class="box-footer">
                           <div class="row">
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ autoVideos.videos.length }}</h5>
                                       <span class="description-text">Videos</span>
                                   </div>
                               </div>
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ autoVideos.view_count }}</h5>
                                       <span class="description-text">Views</span>
                                   </div>
                               </div>
                               <div class="col-sm-4">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ autoVideos.comments_count }}</h5>
                                       <span class="description-text">Comments</span>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </div>
               </div>
               <div class="col-md-4">
                   <div class="box box-widget widget-user">
                       <div class="widget-user-header bg-orange">
                           <h3 class="widget-user-username">Technology</h3>
                           <h5 class="widget-user-desc">High Tech</h5>
                       </div>
                       <div class="widget-user-image">
                           <a href="javascript:void(0)" @click="() => {category = 'Tech'; videos = techVideos}">
                               <img class="img-circle" src="@/assets/tablet.jpg" style="max-width: 90px">
                           </a>
                       </div>
                       <div class="box-footer">
                           <div class="row">
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ techVideos.videos.length }}</h5>
                                       <span class="description-text">Videos</span>
                                   </div>
                               </div>
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ techVideos.view_count }}</h5>
                                       <span class="description-text">Views</span>
                                   </div>
                               </div>
                               <div class="col-sm-4">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ techVideos.comments_count }}</h5>
                                       <span class="description-text">Comments</span>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </div>
               </div>
               <div class="col-md-4">
                   <div class="box box-widget widget-user">
                       <div class="widget-user-header bg-purple">
                           <h3 class="widget-user-username">Miscellaneous</h3>
                           <h5 class="widget-user-desc">Off topic videos</h5>
                       </div>
                       <div class="widget-user-image">
                           <a href="javascript:void(0)" @click="() => {category = 'Other'; videos = otherVideos}">
                               <img class="img-circle" src="@/assets/other.png" style="max-width: 90px">
                           </a>
                       </div>
                       <div class="box-footer">
                           <div class="row">
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ otherVideos.videos.length }}</h5>
                                       <span class="description-text">Videos</span>
                                   </div>
                               </div>
                               <div class="col-sm-4 border-right">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ otherVideos.view_count }}</h5>
                                       <span class="description-text">Views</span>
                                   </div>
                               </div>
                               <div class="col-sm-4">
                                   <div class="description-block">
                                       <h5 class="description-header">{{ otherVideos.comments_count }}</h5>
                                       <span class="description-text">Comments</span>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </div>
               </div>
           </div>

           <videos-list :category="category" :videos="videos" @setVideo="setVideo" v-if="category && videos && !video"></videos-list>

            <video-details v-if="video" :video="video"></video-details>
        </section>
    </div>
</template>

<script>
    import twitter from '@/output/twitter/videos.json'
    import VideosList from '@/components/VideosList'
    import VideoDetails from '@/components/VideoDetails'

    export default {

        components: {VideosList, VideoDetails},

        data() {
            return {
                twitterBased: twitter,
                category: null,
                videos: null,
                video: null
            }
        },

        mounted() {
            $('html, body, .wrapper').css('height', '100%');
        },

        methods: {
            setVideo(video) {
                this.video = video;
            }
        },

        computed: {
            autoVideos() {
                let view_count = 0;
                let comments_count = 0;

                let videos = _.filter(this.twitterBased, lookup => {
                    if (lookup.category === "Autos") {
                        view_count += parseInt(lookup.view_count);
                        comments_count += lookup.comments.length;
                        return true;
                    }
                    return false
                });

                return {
                    view_count: numeral(view_count).format('0.0a'),
                    comments_count: numeral(comments_count).format('0.0a'),
                    videos: videos,
                };
            },

            techVideos() {
                let view_count = 0;
                let comments_count = 0;

                let videos = _.filter(this.twitterBased, lookup => {
                    if (lookup.category === "Tech") {
                        view_count += parseInt(lookup.view_count);
                        comments_count += lookup.comments.length;
                        return true;
                    }
                    return false
                });

                return {
                    view_count: numeral(view_count).format('0.0a'),
                    comments_count: numeral(comments_count).format('0.0a'),
                    videos: videos,
                };
            },

            otherVideos() {
                let view_count = 0;
                let comments_count = 0;

                let videos = _.differenceWith(
                    this.twitterBased,
                    _.concat(this.autoVideos.videos, this.techVideos.videos),
                    _.isEqual
                );

                _.each(videos, videos => {
                    view_count += parseInt(videos.view_count);
                    comments_count += videos.comments.length;
                });

                return {
                    view_count: numeral(view_count).format('0.0a'),
                    comments_count: numeral(comments_count).format('0.0a'),
                    videos: videos,
                };
            }
        }
    }
</script>