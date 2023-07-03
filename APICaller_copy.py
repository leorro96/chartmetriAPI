import ChartmetricAPI.APIConnector as APIConnector
import urllib.parse

class APICaller:
    #Connect API
    def __init__(self,refreshtoken):
        self.session,self.token=APIConnector.connect(refreshtoken)
        self.headers={
             "Authorization": f'Bearer {self.token}'
        }
    def getAlbumCharts(self, platform:str, id:int, since:str=None, until:str=None):
        getAlbumChartsResponse=f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}/{platform}/charts{"?" if (since is not None or until is not None) else ""}{"since="+since if since is not None else ""}{"&" if ((since is not None) and (until is not None)) else ""}{"until="+until if until is not None else ""}'
        return getAlbumChartsResponse
        #IDs
    def getAlbumIDs(self, platform:str, id:int):
        getAlbumIDsResponse=f'https://api.chartmetric.com/api/album/{platform}/{id if isinstance(id, str) else str(id)}/get-ids'
        return getAlbumIDsResponse
        #Metadata
    def getAlbumMetadata(self, id:int):
        getAlbumMetadataResponse=f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}'
        return getAlbumMetadataResponse
        #Playlists        
    def getAlbumPlaylists(self, id:int, platform:str, status:str, since:str, until:str=None, indie:bool=False, limit:int=None, offset:int=None):
        getAlbumPlaylistsResponse=f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}/{platform}/{status}/playlists?since={since}{"&until="+until if until is not None else ""}{"&indie=true" if indie is not False else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}'
        return getAlbumPlaylistsResponse
        #Stats    
    def getAlbumStats(self, id:int, platform:str, stat:str, since:str=None, until:str=None, latest:bool=False):
        getAlbumStatsResponse=f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}/{platform}/{stat}{"?" if ((since is not None) or (until is not None) or (latest is not False)) else ""}{"since="+since if since is not None else ""}{"&" if ((since is not None) and (until is not None or latest is not False)) else ""}{"until="+until if until is not None else ""}{"&" if (until is not None and latest is not False) else ""}{"latest=true" if latest is not False else ""}'
        return getAlbumStatsResponse
        #Tracks            
    def getAlbumTracks(self, id:int):
        getAlbumTracksResponse=f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}/tracks'
        return getAlbumTracksResponse
    #ARTIST
        #ANR - By Social Index
    def getArtistANRbySI(self, sortBy:str, limit:int=None, offset:int=None, code2:str=None, tagIds:int=None, subTagIds:int=None, maxSpotifyFollowers:int=None, sortOrderDesc:bool=False, recentReleaseWithin:int=None, latestReleaseWithin:int=None):
        getArtistANRbySIResponse=f'https://api.chartmetric.com/api/artist/anr/by/social-index?sortBy={sortBy}{"&offset="+str(offset) if offset is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&code2="+code2 if code2 is not None else ""}{"&tagIds="+str(tagIds) if tagIds is not None else ""}{"&subTagIds="+str(subTagIds) if subTagIds is not None else ""}{"&maxSpotifyFollowers="+str(maxSpotifyFollowers) if maxSpotifyFollowers is not None else ""}{"&sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&recentReleaseWithin="+str(recentReleaseWithin) if recentReleaseWithin is not None else ""}{"&latestReleaseWithin="+str(latestReleaseWithin) if latestReleaseWithin is not None else ""}'
        return getArtistANRbySIResponse      
        #ANR - By Playlists
    def getArtistANRbyPlaylists(self, sortBy, streamingType=None, limit=None):
        getArtistANRbyPlaylistsResponse=f'https://api.chartmetric.com/api/artist/anr/by/playlists?sortBy={sortBy}&streamingType={streamingType}{"&limit="+str(limit) if limit is not None else ""}'
        return getArtistANRbyPlaylistsResponse
        #Albums
    def getArtistAlbums(self,id, sortColumn=None, sortOrderDesc=False, offset=None, limit=None):
        getArtistAlbumsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/albums{"?" if ((sortColumn is not None) or (sortOrderDesc is not False) or (offset is not None) or (limit is not None)) else ""}{"sortColumn="+sortColumn if sortColumn is not None else ""}{"&" if sortColumn is not None and (sortOrderDesc is not False or offset is not None or limit is not None) else ""}{"sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&" if sortOrderDesc is not False and (offset is not None or limit is not None) else ""}{"offset="+str(offset) if offset is not None else ""}{"&" if offset is not None and limit is not None else ""}{"limit="+str(limit) if limit is not None else ""}'
        return getArtistAlbumsResponse
        #Rank
    def getArtistRank(self,id, metric=None, code2=None, genre=None):
        getArtistRankResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/artist-rank{"?" if ((metric is not None) or (code2 is not None) or (genre is not None)) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None) and (code2 is not None) else ""}{"code2="+code2 if code2 is not None else ""}{"&" if ((metric is not None) or (code2 is not None)) and genre is not None else ""}{"genre="+str(genre) if genre is not None else ""}'
        return getArtistRankResponse
        #CPP (Cross-Platform Performance)
    def getArtistCPP(self,id, stat, since=None, until=None, latest=False):
        getArtistCPPResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/cpp?stat={stat}{"&since="+since if since is not None else ""}{"&until="+until if until is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getArtistCPPResponse
        #Career History
    def getArtistCareer(self,id, since=None, until=None, limit=None, offset=None):
        getArtistCareerResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/career{"?" if ((since is not None) or (until is not None) or (limit is not None) or (offset is not None)) else ""}{"since="+since if since is not None else ""}{"&" if (since is not None) and (until is not None) else ""}{"until="+until if until is not None else ""}{"&" if (until is not None or since is not None) and (limit is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}'
        return getArtistCareerResponse
        #Charts
    def getArtistCharts(self,id, platform, since, until=None, duration=None):
        getArtistChartsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/{platform}/charts?since={since}&duration={duration}{"&until="+until if until is not None else ""}'
        return getArtistChartsResponse
        #Fan Metrics  
    def getFansMetrics(self,id, source, since=None, until=None, field=None, latest=False, interpolated=False, isDomainId=False, code2=None, city_id=None):
        getFansMetricsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/stat/{source}{"?" if ((since is not None) or (until is not None) or (field is not None) or (latest is not False) or (interpolated is not False) or (isDomainId is not False) or (code2 is not None) or (city_id is not None)) else ""}{"since="+since if since is not None else ""}{"&" if (since is not None) and (until is not None) else ""}{"until="+until if until is not None else ""}{"&" if (since is not None or until is not None) and (field is not None) else ""}{"field="+field if field is not None else ""}{"&" if (since is not None or until is not None or field is not None) and (latest is not False) else ""}{"latest=true" if latest is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False) and (interpolated is not False) else ""}{"interpolated=true" if interpolated is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False) and (isDomainId is not False) else ""}{"isDomainId=true" if isDomainId is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False or isDomainId is not False) and (code2 is not None) else ""}{"code2="+code2 if code2 is not None else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False or isDomainId is not False or code2 is not None) and (city_id is not None) else ""}{"city_id="+str(city_id) if city_id is not None else ""}'
        return getFansMetricsResponse
        #Get Artist IDs
    def getArtistIDs(self,platform, id, limit=None, offset=None, aggregate=False):
        getArtistIDsResponse=f'https://api.chartmetric.com/api/artist/{platform}/{id if isinstance(id, str) else str(id)}/get-ids{"?" if ((limit is not None) or (offset is not None) or (aggregate is not False)) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if (limit is not None) and (offset is not None) else ""}{"offset="+str(offset) if offset is not None else ""}{"&" if (limit is not None or offset is not None) and (aggregate is not False) else ""}{"aggregate=true" if aggregate is not False else ""}'
        return getArtistIDsResponse
        #Get Artist RIAA Awards   
    def getArtistRIAA(self, id):
        getArtistRIAAResponse=f'https://api.chartmetric.com/api/artist/{str(id)}/riaa'
        return getArtistRIAAResponse    
        #Get Artists (with filters)
    #def getArtistsWF(self, tagId:int=None, subTagId:int=None, code2:str=None, firstReleaseDaysAgo:int=None, band:bool=False, pronoun:str=None, sortColumn:str=None, sortOrderDesc:bool=False, sp_p:list=None, sp_f:list=None, dz_fans:list=None, sp_ml:list=None, sp_ratio:list=None, sp_fl_ratio:list=None, tt_f:list=None, tt_l:list=None, fb_f:list=None, fb_l:list=None, fb_t:list=None, tw_f:list=None, tw_r:list=None, ig_f:list=None, ytc_v:list=None, ytc_s:list=None, ytd_vv:list=None, ytm_vv:list=None, wp_v:list=None, sc_f:list=None, bit_f:list=None, cpp:list=None, t_f:list=None, t_v:list=None, t_mvh:list=None, t_wvh:list=None, p_ml:list=None, p_s:list=None, p_ls:list=None, p_lsr:list=None, bp_c:list=None, bp_f:list=None, bp_p:list=None, bp_s:list=None, career_stage:str=None, career_stage_score:list=None, career_trend:str=None, career_trend_score:list=None, limit:int=None, offset:int=None):
     #   getArtistsWFResponse=f'https://api.chartmetric.com/api/artist/list/filter?{"&tagId="+str(tagId) if tagId is not None else ""}{"&subTagId="+str(subTagId) if subTagId is not None else ""}{"&code2="+code2 if code2 is not None else ""}{"&firstReleaseDaysAgo="+str(firstReleaseDaysAgo) if firstReleaseDaysAgo is not None else ""}{"&band=true" if band is not False else ""}{"&pronoun="+pronoun if pronoun is not None else ""}{"&sortColumn="+sortColumn if sortColumn is not None else ""}{"&sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&sp_p="+str(sp_p) if sp_p is not None else ""}{"&sp_f="+str(sp_f) if sp_f is not None else ""}{"&dz_fans="+dz_fans if dz_fans is not None else ""}{"&sp_ml="+sp_ml if sp_ml is not None else ""}{"&sp_ratio="+sp_ratio if sp_ratio is not None else ""}{"&sp_fl_ratio="+sp_fl_ratio if sp_fl_ratio is not None else ""}{"&tt_f="+tt_f if tt_f is not None else ""}{"&tt_l="+tt_l if tt_l is not None else ""}{"&fb_f="+fb_f if fb_f is not None else ""}{"&fb_l="+fb_l if fb_l is not None else ""}{"&fb_t="+fb_t if fb_t is not None else ""}{"&tw_f="+tw_f if tw_f is not None else ""}{"&tw_r="+tw_r if tw_r is not None else ""}{"&ig_f="+ig_f if ig_f is not None else ""}{"&ytc_v="+ytc_v if ytc_v is not None else ""}{"&ytc_s="+ytc_s if ytc_s is not None else ""}{"&ytd_vv="+ytd_vv if ytd_vv is not None else ""}{"&ytm_vv="+ytm_vv if ytm_vv is not None else ""}{"&wp_v="+wp_v if wp_v is not None else ""}{"&sc_f="+sc_f if sc_f is not None else ""}{"&bit_f="+bit_f if bit_f is not None else ""}{"&cpp="+cpp if bit_f is not None else ""}{"&t_f="+t_f if t_f is not None else ""}{"&t_v="+t_v if t_v is not None else ""}{"&t_mvh="+t_mvh if t_mvh is not None else ""}{"&t_wvh="+t_wvh if t_wvh is not None else ""}{"&p_ml="+p_ml if p_ml is not None else ""}{"&p_ls="+p_ls if p_ls is not None else ""}{"&p_lsr="+p_lsr if p_lsr is not None else ""}{"&bp_c="+bp_c if bp_c is not None else ""}{"&bp_f="+bp_f if bp_f is not None else ""}{"&bp_p="+bp_p if bp_p is not None else ""}{"&bp_s="+bp_s if bp_s is not None else ""}{"&career_stage="+career_stage if career_stage is not None else ""}{"&career_stage_score="+career_stage_score if career_stage_score is not None else ""}{"&career_trend="+career_trend if career_trend is not None else ""}{"&career_trend_score="+career_trend_score if career_trend_score is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}'
      #  return getArtistsWFResponse
        #Get Artists
    def getArtists(self, platform:str, min:int, max:int, code2:str, genreId:int, subGenreId:int, city:str, unsigned:bool=False, limit:int=None, offset:int=None):
        getArtistsResponse=f'https://api.chartmetric.com/api/artist/{platform}/list?min={min}&max={max}&code2={code2}&genreId={genreId}&subGenreId={subGenreId}&city={city}{"&unsigned=true" if unsigned is not False else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}'
        return getArtistsResponse
        #Historical Artist Rank
    def getArtistsHAR(self, id:int, metric:str=None, date:str=None):
        getArtistsHARResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/past-artist-rank{"?" if (metric is not None or date is not None) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None and date is not None) else ""}{"date="+date if date is not None else ""}'
        return getArtistsHARResponse
        #Instagram Audience Data Dates
    def getArtistsIGAudienceDates(self, id:int):
        getArtistsIGAudienceDatesResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/instagram-audience-stats/dates'
        return getArtistsIGAudienceDatesResponse
        #Instagram Audience Data 
    def getArtistsIGAudienceData(self, id:int, date:str=None, geoOnly:bool=False):
        getArtistsIGAudienceDataResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/instagram-audience-stats{"?" if (date is not None or geoOnly is not False) else ""}{"date="+date if date is not None else ""}{"&" if (date is not None and geoOnly is not False) else ""}{"geoOnly=true" if geoOnly is not False else ""}'
        return getArtistsIGAudienceDataResponse
        #Artist Metadata
    def getArtistsMetadata(self, id:int):
        getArtistsMetadataResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}'
        return getArtistsMetadataResponse
        #Artist Neighbouring Artists
    def getArtistsNeighbors(self, id:int, metric:str=None, limit:int=None, genreType:str=None):
        getArtistsNeighborsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/neighboring-artists{"?" if (metric is not None or limit is not None or genreType is not None) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None and limit is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if ((limit is not None or metric is not None) and genreType is not None) else ""}{"type="+str(genreType) if genreType is not None else ""}'
        return getArtistsNeighborsResponse
        #Artist Playlists
    def getArtistsPlaylists(self, id:int, platform:str, status, since=None, until=None, indie=None, editorial=None, majorCurator=None, limit=None, offset=None):
        getArtistsPlaylistsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/{platform}/{status}/playlists{"?" if (since is not None or until is not None or indie is not None or editorial is not None or majorCurator is not None or limit is not None or offset) else ""}{"since="+since if since is not None else ""}'
        return getArtistsPlaylistsResponse    
        #Artist Related Artists
    def getArtistsRelatedArtists(self, id:int, limit:int=None, fromDaysAgo:int=None, toDaysAgo:int=None):
        getArtistsRelatedArtistsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/relatedartists{"?" if (limit is not None or fromDaysAgo is not None or toDaysAgo is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if limit is not None and fromDaysAgo is not None else ""}{"fromDaysAgo="+str(fromDaysAgo) if fromDaysAgo is not None else ""}{"&" if (fromDaysAgo is not None or limit is not None) and toDaysAgo is not None else ""}{"toDaysAgo="+str(toDaysAgo) if toDaysAgo is not None else ""}'
        return getArtistsRelatedArtistsResponse
        #Artist Social / Streaming Service URLs
    def getArtistSocials(self,id:int):
        getArtistSocialsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/urls'
        return getArtistSocialsResponse
        #Artist Social Audience Stats
    def getArtistSocialAudienceStats(self,id, audienceType, statsType, domain, since=None, until=None, offset=None, limit=None):
        getArtistSocialAudienceStatsResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/social-audience-stats?domain={domain}&audienceType={audienceType}&statsType={statsType}{"&since="+since if since is not None else ""}{"&until="+until if until is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&limit="+str(limit) if limit is not None else ""}'
        return getArtistSocialAudienceStatsResponse
        #Artist Spotify Monthly Listeners by City
    def getArtistSpotifyMLbyCity(self,id, since, until=None, latest=False, showHistory=False, offset=None, limit=None):
        getArtistSpotifyMLbyCityResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/where-people-listen?since={since}{"&until="+str(until) if until is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}{"&showHistory=true" if showHistory is not False else ""}'
        return getArtistSpotifyMLbyCityResponse
        #Artist TV Show Appearances
    def getArtistTVShowAppearances(self,id):
        getArtistTVShowAppearancesResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tvmaze'
        return getArtistTVShowAppearancesResponse
        #Artist Tiktok Audience Data
    def getArtistTiktokAudienceData(self,id, date=None):
        getArtistTiktokAudienceDataResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tiktok-audience-stats{"?date="+date if date is not None else ""}'
        return getArtistTiktokAudienceDataResponse
        #Artist Top Tracks by Platform
    def getArtistTopTracks(self,id, source, limit=None):
        getArtistTopTracksResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/top-tracks/{source}{"?limit="+str(limit) if limit is not None else ""}'
        return getArtistTopTracksResponse        
        #Artist Tracks
    def getArtistTracks(self,id, offset=None, limit=None, artistType=None):
        getArtistTracksResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tracks{"?" if offset is not None or limit is not None or artistType is not None else ""}{"offset="+str(offset) if offset is not None else ""}{"&" if offset is not None and limit is not None else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if (limit is not None or offset is not None) and artistType is not None else ""}{"artist_type="+artistType if artistType is not None else ""}'
        return getArtistTracksResponse
        #Artist Youtube Audience Data
    def getArtistYoutubeAudience(self,id, date=None, geoOnly=False):
        getArtistYoutubeAudienceResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/youtube-audience-stats{"?" if date is not None or geoOnly is not False else ""}{"date="+date if date is not None else ""}{"&" if date is not None and geoOnly is not False else ""}{"geoOnly=true" if geoOnly is not False else ""}'
        return getArtistYoutubeAudienceResponse
        #Artist Youtube Views and Market Coverage
    def getArtistYoutubeViewsAndCoverage(self,id):
        getArtistYoutubeViewsAndCoverageResponse=f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/market-coverage-views/youtube'
        return getArtistYoutubeViewsAndCoverageResponse
    #BRAND
        #Brand Info
    def getBrandInfo(self,id,sortColumn=None, sortOrderDesc=False, limit=None, offset=None):
        getBrandInfoResponse=f'https://api.chartmetric.com/api/brand/{id if isinstance(id, str) else str(id)}{"?" if sortColumn is not None or sortOrderDesc is not False or limit is not None or offset is not None else ""}{"sortColumn="+sortColumn if sortColumn is not None else ""}{"&" if sortColumn is not None and (sortOrderDesc is not False or limit is not None or offset is not None) else ""}{"sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&" if sortOrderDesc is not False and (limit is not None or offset is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if limit is not None and offset is not None else ""}{"offset="+str(offset) if offset is not None else ""}'
        return getBrandInfoResponse
        #Brand List by Interest
    def getBrandListbyInterest(self, sortColumn=None):
        getBrandListbyInterestResponse=f'https://api.chartmetric.com/api/brand/list/by/interest{"?sortColumn="+sortColumn if sortColumn is not None else ""}'
        return getBrandListbyInterestResponse
        #Brand List
    def getBrandList(self):
        getBrandListResponse=f'https://api.chartmetric.com/api/brand/list'
        return getBrandListResponse
    #CHARTS

        #Charts Airplay
    def getChartsAirplay(self, chart_type:str, date:str, since:str, limit, duration, country_code=None, latest=False):
        getChartsAirplayResponse=f'https://api.chartmetric.com/api/charts/airplay/{chart_type}?date={date}&since={since}&limit={limit}&duration={duration}{"&country_code="+country_code if country_code is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsAirplayResponse    
        #Charts Amazon
    def getChartsAmazon(self, chart_type, sub_type, date, genre, code2=None, offset=None, latest=False):
        genre="+".join(genre.split(" "))
        getChartsAmazonResponse=f'https://api.chartmetric.com/api/charts/amazon/{chart_type}?type={sub_type}&date={date}&genre={genre}{"&code2="+code2 if code2 is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsAmazonResponse
        #Charts Apple Music
    def getChartsAppleMusic(self, chart_type:str, sub_type:str, date:str, code2:str, city_id:int=None, genre:str=None, offset:int=None, latest:bool=False):
        genre="+".join(genre.split(" ")) if genre else None
        getChartsAppleMusicResponse=f'https://api.chartmetric.com/api/charts/applemusic/{chart_type}?type={sub_type}&date={date}&country_code={code2}{"&city_id="+str(city_id) if city_id is not None else ""}{"&genre="+genre if genre is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsAppleMusicResponse
        #Charts Beatport
    def getChartsBeatport(self, date, genre, offset=None, latest=False):
        getChartsBeatportResponse=f'https://api.chartmetric.com/api/charts/beatport?date={date}&genre={genre}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsBeatportResponse
        #Charts Countries
    def getChartsCountries(self, platform, chart_type, sub_type, duration):
        getChartsCountriesResponse=f'https://api.chartmetric.com/api/charts/{platform}/countries?chart_type={chart_type}&type={sub_type}&duration={duration}'
        return getChartsCountriesResponse        
        #Charts Chartmetric Score
    def getChartsChartmetricScore(self, asset_type, type_id, chart_type, since, until=None):
        getChartsChartmetricScoreResponse=f'https://api.chartmetric.com/api/charts/{asset_type}/{type_id}/{chart_type}/cm-score?since={since}{"&until="+until if until is not None else ""}'
        return getChartsChartmetricScoreResponse        
        #Charts Deezer
    def getChartsDeezer(self, country_code, date, latest=False):
        getChartsDeezerResponse=f'https://api.chartmetric.com/api/charts/deezer?country_code={country_code}&date={date}{"&latest=true" if latest is not False else ""}'
        return getChartsDeezerResponse
        #Charts QQ Music
    def getChartsQQMusic(self, date, latest=False):
        getChartsQQMusicResponse=f'https://api.chartmetric.com/api/charts/qq?date={date}{"&latest=true" if latest is not False else ""}'
        return getChartsQQMusicResponse
        #Charts Shazam (Cities)
    def getChartsShazamCities(self, country_code):
        getChartsQQMusicResponse=f'https://api.chartmetric.com/api/charts/shazam/{country_code}/cities'
        return getChartsQQMusicResponse
        #Charts Shazam 
    def getChartsShazam(self, country_code, date, city=None, offest=None, latest=False):
        getChartsShazamResponse=f'https://api.chartmetric.com/api/charts/shazam?date={date}&country_code={country_code}{"&city="+urllib.parse.quote(city) if city is not None else ""}{"&offset="+str(offest) if offest is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsShazamResponse
        #Charts SoundCloud 
    def getChartsSoundCloud(self, country_code, date, kind, genre, offest=None, raw=False, latest=False):
        getChartsSoundCloudResponse=f'https://api.chartmetric.com/api/charts/soundcloud?date={date}&country_code={country_code}&kind={kind}&genre={genre}{"&offset="+str(offest) if offest is not None else ""}{"&raw=true" if raw is not False else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsSoundCloudResponse
        #Charts Spotify (Artists) 
    def getChartsSpotifyArtists(self, date, chart_type, interval, offest=None, latest=False):
        getChartsSpotifyArtistsResponse=f'https://api.chartmetric.com/api/charts/spotify/artists?date={date}&interval={interval}&type={chart_type}{"&offset="+str(offest) if offest is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsSpotifyArtistsResponse
        #Charts Spotify (Freshfind) 
    def getChartsSpotifyFreshfind(self, date, latest=False):
        getChartsSpotifyFreshfindResponse=f'https://api.chartmetric.com/api/charts/spotify/freshfind?date={date}{"&latest=true" if latest is not False else ""}'
        return getChartsSpotifyFreshfindResponse
        #Charts Spotify (Tracks) 
    def getChartsSpotifyTracks(self, date:str, country_code:str, chart_type:str, interval:str, offset:int=None, latest:bool=False):
        getChartsSpotifyTracksResponse=f'https://api.chartmetric.com/api/charts/spotify?date={date}&country_code={country_code}&interval={interval}&type={chart_type}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsSpotifyTracksResponse
        #Charts Tiktok Top Tracks Stats (Freq Update)
    def getChartsTiktokTopTracksStats(self, date, limit=None, offset=None):
        getChartsTiktokTopTracksStatsResponse=f'https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date={date}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}'
        return getChartsTiktokTopTracksStatsResponse        
        #Charts Tiktok 
    def getChartsTiktok(self, chart_type:str, date:str, user_chart_type:str, interval:str=None, limit:int=None, offset:int=None, latest:bool=False, countryChart:str=False, code2:str=None):
        getChartsTiktokResponse=f'https://api.chartmetric.com/api/charts/tiktok/{chart_type}?date={date}{"&type="+user_chart_type if chart_type=="users" else ""}{"&interval="+interval if interval is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}{"&countryChart=true" if countryChart is not False else ""}{"&code2="+code2 if (countryChart is not False) and (code2 is not None) else ""}'
        return getChartsTiktokResponse
        #Charts Twitch
    def getChartsTwitch(self, since, limit, duration, chart_type, date=None, latest=False):
        getChartsTwitchResponse=f'https://api.chartmetric.com/api/charts/twitch/users?since={since}&type={chart_type}&duration={duration}&limit={limit}{"&date="+date if date is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsTwitchResponse
        #Charts Youtube
    def getChartsYoutube(self, chart_type, country_code, date, offset=None, latest:bool=False):
        getChartsYoutubeResponse=f'https://api.chartmetric.com/api/charts/youtube/{chart_type}?date={date}&country_code={country_code}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsYoutubeResponse
        #Charts iTunes 
    def getChartsiTunes(self, chart_type, country_code, date, genre, offset=None, latest=False):
        getChartsiTunesResponse=f'https://api.chartmetric.com/api/charts/itunes/{chart_type}?date={date}&country_code={country_code}&genre={genre}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}'
        return getChartsiTunesResponse
    #CITY

        #Top Artists
    def getCityTopArtists(self, id, source):
        getCityTopArtistsResponse=f'https://api.chartmetric.com/api/city/{id}/{source}/top-artists'
        return getCityTopArtistsResponse
        #Top Tracks
    def getCityTopTracks(self, id, source):
        getCityTopTracksResponse=f'https://api.chartmetric.com/api/city/{id}/{source}/top-tracks'
        return getCityTopTracksResponse
    #CURATOR

        #Curator List
    def getCuratorList(self, platform, offset=None, limit=None, editorial=None, majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None):
        getCuratorListResponse=f'https://api.chartmetric.com/api/curator/{platform}/lists'
        return getCuratorListResponse
        #Curator Fan Metrics
    def getCuratorFanMetrics(self, id, platform, source, since=None, until=None, field=None, latest=None, interpolated=None):
        getCuratorFanMetricsResponse=f'https://api.chartmetric.com/api/curator/{platform}/{id}/stat/{source}'
        return getCuratorFanMetricsResponse
        #Curator Metadata
    def getCuratorMetadata(self, id, platform):
        getCuratorMetadataResponse=f'https://api.chartmetric.com/api/curator/{platform}/{id}/'
        return getCuratorMetadataResponse
        #Curator Playlists
    def getCuratorPlaylists(self, id, platform, limit=None, offset=None):
        getCuratorPlaylistsResponse=f'https://api.chartmetric.com/api/curator/{platform}/{id}/playlists'
        return getCuratorPlaylistsResponse
        #Curator Social / Streaming Service URLs
    def getCuratorSocialStreamingURLs(self, id, platform):
        getCuratorSocialStreamingURLsResponse=f'https://api.chartmetric.com/api/curator/{platform}/{id}/urls'
        return getCuratorSocialStreamingURLsResponse
    #PLAYLIST
    
        #Playlist Metadata
    def getPlaylistMetadata(self, id, platform, storefront=None):
        getPlaylistMetadataResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}'
        return getPlaylistMetadataResponse
        #Playlist Evolution Stats (given Artist, Album or Track Chartmetric ID)
    def getPlaylistEvolutionStats(self, type, id, since=None, until=None):
        getPlaylistEvolutionStatsResponse=f'https://api.chartmetric.com/api/playlist/by/{type}/{id}/evolution'
        return getPlaylistEvolutionStatsResponse
        #Playlist Journey or Progression
    def getPlaylistJourneyProgression(self, platform, type, id, sortColumn=None, sortOrderDesc=None, limit=None, offset=None):
        getPlaylistJourneyProgressionResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/journey-progression/{type}'
        return getPlaylistJourneyProgressionResponse
        #Playlist Last Updated Time
    def getPlaylistLastUpdatedTime(self, platform, id, storefron=None):
        getPlaylistLastUpdatedTimeResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/updated'
        return getPlaylistLastUpdatedTimeResponse
        #Playlist List
    def getPlaylistList(self, platform, sortColumn=None, sortOrderDesc=None, code2=None, tagIds=None, curatorIds=None, limit=None, offset=None, indie=None, majorCurator=None, editorial=None, newMusicFriday=None):
        getPlaylistListResponse=f'https://api.chartmetric.com/api/playlist/{platform}/lists?limit=100&offset=9900&sortColumn=followers'
        return getPlaylistListResponse        
        #Playlist Snapshot
    def getPlaylistSnapshot(self, id, platform, date, storefront=None):
        getPlaylistSnapshotResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/snapshot?date={date}'
        return getPlaylistSnapshotResponse
        #Playlist Stats Over Time
    def getPlaylistStatsOverTime(self, id, platform, since, until=None):
        getPlaylistStatsOverTimeResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/stats?since={since}'
        return getPlaylistStatsOverTimeResponse
        #Playlist Tracks (Current, Past)
    def getPlaylistTracks(self, id, platform, span, storefront=None, offset=None, withDetails=None, since=None, until=None):
        getPlaylistTracksResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/{span}/tracks'
        return getPlaylistTracksResponse
    #RADIO
    
        #Radio Airplay information in Time Series
    def getRadioAirplayInfoinTime(self, id, type, since):
        getRadioAirplayInfoinTimeResponse=f'https://api.chartmetric.com/api/radio/{type}/{id}/airplays?since={since}'
        return getRadioAirplayInfoinTimeResponse
        #Radio Broadcast Market play counts
    def getRadioBroadcastPlayCounts(self, id, type, since):
        getRadioBroadcastPlayCountsResponse=f'https://api.chartmetric.com/api/radio/{type}/{id}/broadcast-markets?since={since}'
        return getRadioBroadcastPlayCountsResponse
        #Get Radio Station List for Country
    def getRadioStationList(self, code2=None):
        getRadioStationListResponse=f'https://api.chartmetric.com/api/radio/station-list?code2={code2}'
        return getRadioStationListResponse
        #Radio Total Airplays
    def getRadioTotalAirplay(self, id, type, since, limit=None):
        getRadioTotalAirplayResponse=f'https://api.chartmetric.com/api/radio/{type}/{id}/airplay-totals?limit={limit}&since={since}'
        return getRadioTotalAirplayResponse
    #RECOMMENDATION

        #Get 100 Similar Playlists
    def getRecommendationSimilarPlaylists(self, id, platform, storefront=None, indie=None, limit=None):
        getRecommendationSimilarPlaylistsResponse=f'https://api.chartmetric.com/api/playlist/{platform}/{id}/similarplaylists'
        return getRecommendationSimilarPlaylistsResponse
    #SEARCH

        #Chartmetric Search Engine
    def search(self, q, limit=None, offset=None, type=None):
        searchResponse=f'https://api.chartmetric.com/api/search?q={q}'
        return searchResponse
        #Get City Info
    def getCityInfo(self, country_code):
        getCityInfoResponse=f'https://api.chartmetric.com/api/cities?country_code={country_code}'
        return getCityInfoResponse
        #Get Genre Ids
    def getGenreIds(self, name=None):
        getGenreIdsResponse=f'https://api.chartmetric.com/api/genres?name={name}'
        return getGenreIdsResponse
    #TRACK 

        #Track Charts
    def getTrackCharts(self, type, id, since, until=None):
        getTrackChartsResponse=f'https://api.chartmetric.com/api/track/{id}/{type}/charts?since={since}'
        return getTrackChartsResponse
        #Track Get Track IDs
    def getTrackIDs(self, type, id):
        getTrackIDsResponse=f'https://api.chartmetric.com/api/track/{type}/{id}/get-ids'
        return getTrackIDsResponse
        #Track Get Tracks (with filters)
    def getTracksWFilter(self, limit=None,offset=None,sortOrderDesc=None,sortColumn=None,genres=None,artists=None,range_period=None,max_score=None,min_score=None,max_release_date=None,min_release_date=None,max_airplay_streams=None,min_airplay_streams=None,max_amazon_playlist_count=None,min_amazon_playlist_count=None,max_deezer_playlist_count=None,min_deezer_playlist_count=None,max_itunes_playlist_count=None,min_itunes_playlist_count=None,max_shazam_count=None,min_shazam_count=None,max_siriusxm_streams=None,min_siriusxm_streams=None,max_soundcloud_plays=None,min_soundcloud_plays=None,max_spotify_playlist_count=None,min_spotify_playlist_count=None,max_spotify_plays=None,min_spotify_plays=None,max_spotify_popularity=None,min_spotify_popularity=None,max_tiktok_posts=None,min_tiktok_posts=None,max_tiktok_top_videos_likes=None,min_tiktok_top_videos_likes=None,max_tiktok_top_videos_views=None,min_tiktok_top_videos_views=None,max_youtube_likes=None,min_youtube_likes=None,max_youtube_playlist_count=None,min_youtube_playlist_count=None):
        getTracksWFilterResponse=f'https://api.chartmetric.com/api/track/list/filter'
        return getTracksWFilterResponse
        #Track Get Metadata
    def getTrackMetadata(self, id):
        getTrackMetadataResponse=f'https://api.chartmetric.com/api/track/{id}'
        return getTrackMetadataResponse
        #Track Playlist Snapshot
    def getTrackPlaylistSnapshot(self, id,platform,storefront=None,limit=None,offset=None):
        getTrackPlaylistSnapshotResponse=f'https://api.chartmetric.com/api/track/{id}/{platform}/playlists/snapshot'
        return getTrackPlaylistSnapshotResponse
        #Track Playlist 
    def getTrackPlaylists(self, id,platform,status,since=None,until=None,indie=None,limit=None,offset=None,sortColumn=None,editorial=None,majorCurator=None):
        getTrackPlaylistsResponse=f'https://api.chartmetric.com/api/track/{id}/{platform}/{status}/playlists'
        return getTrackPlaylistsResponse
        #Track Related Tracks 
    def getTrackRelatedTracks(self, id):
        getTrackRelatedTracksResponse=f'https://api.chartmetric.com/api/track/{id}/relatedTracks'
        return getTrackRelatedTracksResponse
        #Track Stats 
    def getTrackStats(self, id,platform,mode,since=None,until=None,latest=None,interpolated=None,type=None,isDomainId=None):
        getTrackStatsResponse=f'https://api.chartmetric.com/api/track/{id}/{platform}/stats/{mode}'
        return getTrackStatsResponse
        #Track Top TikTok Video 
    def getTrackTopTikTokVideo(self, id, limit=None,type=None):
        getTrackTopTikTokVideoResponse=f'https://api.chartmetric.com/api/track/{id}/topVideos'
        return getTrackTopTikTokVideoResponse