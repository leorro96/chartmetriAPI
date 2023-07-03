import ChartmetricAPI.APIConnector as APIConnector
import urllib.parse
import requests

class APICaller:
    #Connect API
    def __init__(self,refreshtoken):
        self.session,self.token=APIConnector.connect(refreshtoken)
        self.headers={
             "Authorization": f'Bearer {self.token}'
        }
    
    #ALBUM
        #Charts
    def getAlbumCharts(self, platform:str, id:int, since:str=None, until:str=None):
            #Since and Until format --> (string) 2020-03-01
        try:
            getAlbumChartsResponse=self.session.get(f'https://api.chartmetric.com/api/album/{str(id)}/{platform}/charts{"?" if (since is not None or until is not None) else ""}{"since="+since if since is not None else ""}{"&" if ((since is not None) and (until is not None)) else ""}{"until="+until if until is not None else ""}',headers=self.headers)
            getAlbumChartsResponse.raise_for_status()
            return getAlbumChartsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        #IDs
    def getAlbumIDs(self, platform:str, id:int):
        try:
            getAlbumIDsResponse=self.session.get(f'https://api.chartmetric.com/api/album/{platform}/{str(id)}/get-ids',headers=self.headers)
            getAlbumIDsResponse.raise_for_status()
            return getAlbumIDsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        #Metadata
    def getAlbumMetadata(self, id:int):
        try:
            getAlbumMetadataResponse=self.session.get(f'https://api.chartmetric.com/api/album/{str(id)}',headers=self.headers)
            getAlbumMetadataResponse.raise_for_status()
            return getAlbumMetadataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        #Playlists        
    def getAlbumPlaylists(self, id:int, platform:str, status:str, since:str, until:str=None, indie:bool=False, limit:int=None, offset:int=None):
        try:
            getAlbumPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/album/{id if isinstance(id, str) else str(id)}/{platform}/{status}/playlists?since={since}{"&until="+until if until is not None else ""}{"&indie=true" if indie is not False else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}',headers=self.headers)
            print(f'https://api.chartmetric.com/api/album/{str(id)}/{platform}/{status}/playlists?since={since}{"&until="+until if until is not None else ""}{"&indie=true" if indie is not False else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}')
            getAlbumPlaylistsResponse.raise_for_status()
            return getAlbumPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)  
        #Stats    
    def getAlbumStats(self, id:int, platform:str, stat:str, since:str=None, until:str=None, latest:bool=False):
        try:
            getAlbumStatsResponse=self.session.get(f'https://api.chartmetric.com/api/album/{str(id)}/{platform}/{stat}{"?" if ((since is not None) or (until is not None) or (latest is not False)) else ""}{"since="+since if since is not None else ""}{"&" if ((since is not None) and (until is not None or latest is not False)) else ""}{"until="+until if until is not None else ""}{"&" if (until is not None and latest is not False) else ""}{"latest=true" if latest is not False else ""}',headers=self.headers)
            getAlbumStatsResponse.raise_for_status()
            return getAlbumStatsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        #Tracks            
    def getAlbumTracks(self, id:int):
        try:
            getAlbumTracksResponse=self.session.get(f'https://api.chartmetric.com/api/album/{str(id)}/tracks',headers=self.headers)
            getAlbumTracksResponse.raise_for_status()
            return getAlbumTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__) 


    #ARTIST
        #ANR - By Social Index
    def getArtistANRbySI(self, sortBy:str, limit:int=None, offset:int=None, code2:str=None, tagIds:int=None, subTagIds:int=None, maxSpotifyFollowers:int=None, sortOrderDesc:bool=False, recentReleaseWithin:int=None, latestReleaseWithin:int=None):
        try:
            getArtistANRbySIResponse=self.session.get(f'https://api.chartmetric.com/api/artist/anr/by/social-index?sortBy={sortBy}{"&offset="+str(offset) if offset is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&code2="+code2 if code2 is not None else ""}{"&tagIds="+str(tagIds) if tagIds is not None else ""}{"&subTagIds="+str(subTagIds) if subTagIds is not None else ""}{"&maxSpotifyFollowers="+str(maxSpotifyFollowers) if maxSpotifyFollowers is not None else ""}{"&sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&recentReleaseWithin="+str(recentReleaseWithin) if recentReleaseWithin is not None else ""}{"&latestReleaseWithin="+str(latestReleaseWithin) if latestReleaseWithin is not None else ""}',headers=self.headers)
            getArtistANRbySIResponse.raise_for_status()
            return getArtistANRbySIResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)   
              
        #ANR - By Playlists
    def getArtistANRbyPlaylists(self, sortBy:str, streamingType:str, limit:int=None):
        try:
            getArtistANRbyPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/anr/by/playlists?sortBy={sortBy}&streamingType={streamingType}{"&limit="+str(limit) if limit is not None else ""}', headers=self.headers)
            getArtistANRbyPlaylistsResponse.raise_for_status()
            return getArtistANRbyPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Albums
    def getArtistAlbums(self,id:int, sortColumn:str=None, sortOrderDesc:bool=False, offset:int=None, limit:int=None):
        try:
            getArtistAlbumsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/albums{"?" if ((sortColumn is not None) or (sortOrderDesc is not False) or (offset is not None) or (limit is not None)) else ""}{"sortColumn="+sortColumn if sortColumn is not None else ""}{"&" if sortColumn is not None and (sortOrderDesc is not False or offset is not None or limit is not None) else ""}{"sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&" if sortOrderDesc is not False and (offset is not None or limit is not None) else ""}{"offset="+str(offset) if offset is not None else ""}{"&" if offset is not None and limit is not None else ""}{"limit="+str(limit) if limit is not None else ""}',headers=self.headers)
            getArtistAlbumsResponse.raise_for_status()
            return getArtistAlbumsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Rank
    def getArtistRank(self,id:int, metric:str=None, code2:str=None, genre:int=None):
        try:
            getArtistRankResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/artist-rank{"?" if ((metric is not None) or (code2 is not None) or (genre is not None)) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None) and (code2 is not None) else ""}{"code2="+code2 if code2 is not None else ""}{"&" if ((metric is not None) or (code2 is not None)) and genre is not None else ""}{"genre="+str(genre) if genre is not None else ""}',headers=self.headers)
            getArtistRankResponse.raise_for_status()
            return getArtistRankResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__) 

        #CPP (Cross-Platform Performance)
    def getArtistCPP(self,id:int, stat:str, since:str=None, until:str=None, latest:str=False):
        try:
            getArtistCPPResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/cpp?stat={stat}{"&since="+since if since is not None else ""}{"until="+until if until is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getArtistCPPResponse.raise_for_status()
            return getArtistCPPResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Career History
    def getArtistCareer(self,id:int, since:str=None, until:str=None, limit:int=None, offset:int=None):
        try:
            getArtistCareerResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/career{"?" if ((since is not None) or (until is not None) or (limit is not None) or (offset is not None)) else ""}{"since="+since if since is not None else ""}{"&" if (since is not None) and (until is not None) else ""}{"until="+until if until is not None else ""}{"&" if (until is not None or since is not None) and (limit is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}',headers=self.headers)
            getArtistCareerResponse.raise_for_status()
            return getArtistCareerResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__) 

        #Charts
    def getArtistCharts(self,id:int, platform:str, since:str, duration:str, until:str=None):
        try:
            getArtistChartsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/{platform}/charts?since={since}&duration={duration}{"&until="+until if until is not None else ""}',headers=self.headers)
            getArtistChartsResponse.raise_for_status()
            return getArtistChartsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__) 

        #Fan Metrics  
    def getFansMetrics(self,id:int, source:str, since:str=None, until:str=None, field:str=None, latest:bool=False, interpolated:bool=False, isDomainId:bool=False, code2:str=None, city_id:int=None):
        try:
            getFansMetricsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/stat/{source}{"?" if ((since is not None) or (until is not None) or (field is not None) or (latest is not False) or (interpolated is not False) or (isDomainId is not False) or (code2 is not None) or (city_id is not None)) else ""}{"since="+since if since is not None else ""}{"&" if (since is not None) and (until is not None) else ""}{"until="+until if until is not None else ""}{"&" if (since is not None or until is not None) and (field is not None) else ""}{"field="+field if field is not None else ""}{"&" if (since is not None or until is not None or field is not None) and (latest is not False) else ""}{"latest=true" if latest is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False) and (interpolated is not False) else ""}{"interpolated=true" if interpolated is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False) and (isDomainId is not False) else ""}{"isDomainId=true" if isDomainId is not False else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False or isDomainId is not False) and (code2 is not None) else ""}{"code2="+code2 if code2 is not None else ""}{"&" if (since is not None or until is not None or field is not None or latest is not False or interpolated is not False or isDomainId is not False or code2 is not None) and (city_id is not None) else ""}{"city_id="+str(city_id) if city_id is not None else ""}',headers=self.headers)
            getFansMetricsResponse.raise_for_status()
            return getFansMetricsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
    
        #Get Artist IDs
    def getArtistIDs(self,platform:str, id:int, limit:int=None, offset:int=None, aggregate:bool=False):
        try:
            getArtistIDsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{platform}/{str(id)}/get-ids{"?" if ((limit is not None) or (offset is not None) or (aggregate is not False)) else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&aggregate=true" if aggregate is not False else ""}',headers=self.headers)
            getArtistIDsResponse.raise_for_status()
            return getArtistIDsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get Artist RIAA Awards   
    def getArtistRIAA(self, id:int):
        try:
            getArtistRIAAResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{str(id)}/riaa',headers=self.headers)
            getArtistRIAAResponse.raise_for_status()
            return getArtistRIAAResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get Artists (with filters)
    #def getArtistsWF(self, tagId:int=None, subTagId:int=None, code2:str=None, firstReleaseDaysAgo:int=None, band:bool=False, pronoun:str=None, sortColumn:str=None, sortOrderDesc:bool=False, sp_p:list=None, sp_f:list=None, dz_fans:list=None, sp_ml:list=None, sp_ratio:list=None, sp_fl_ratio:list=None, tt_f:list=None, tt_l:list=None, fb_f:list=None, fb_l:list=None, fb_t:list=None, tw_f:list=None, tw_r:list=None, ig_f:list=None, ytc_v:list=None, ytc_s:list=None, ytd_vv:list=None, ytm_vv:list=None, wp_v:list=None, sc_f:list=None, bit_f:list=None, cpp:list=None, t_f:list=None, t_v:list=None, t_mvh:list=None, t_wvh:list=None, p_ml:list=None, p_s:list=None, p_ls:list=None, p_lsr:list=None, bp_c:list=None, bp_f:list=None, bp_p:list=None, bp_s:list=None, career_stage:str=None, career_stage_score:list=None, career_trend:str=None, career_trend_score:list=None, limit:int=None, offset:int=None):
    #    try:
    #        getArtistsWFResponse=self.session.get(f'https://api.chartmetric.com/api/artist/list/filter?{"&tagId="+tagId if tagId is not None else ""}{"&subTagId="+subTagId if subTagId is not None else ""}{"&code2="+code2 if code2 is not None else ""}{"&firstReleaseDaysAgo="+firstReleaseDaysAgo if firstReleaseDaysAgo is not None else ""}{"&band="+band if band is not False else ""}{"&pronoun="+pronoun if pronoun is not None else ""}{"&sortColumn="+sortColumn if sortColumn is not None else ""}{"&sortOrderDesc="+sortOrderDesc if sortOrderDesc is not False else ""}{"&sp_p="+sp_p if sp_p is not None else ""}{"&sp_f="+sp_f if sp_f is not None else ""}{"&dz_fans="+dz_fans if dz_fans is not None else ""}{"&sp_ml="+sp_ml if sp_ml is not None else ""}{"&sp_ratio="+sp_ratio if sp_ratio is not None else ""}{"&sp_fl_ratio="+sp_fl_ratio if sp_fl_ratio is not None else ""}{"&tt_f="+tt_f if tt_f is not None else ""}{"&tt_l="+tt_l if tt_l is not None else ""}{"&fb_f="+fb_f if fb_f is not None else ""}{"&fb_l="+fb_l if fb_l is not False else ""}{"&fb_t="+fb_t if fb_t is not None else ""}{"&tw_f="+tw_f if tw_f is not None else ""}{"&tw_r="+tw_r if tw_r is not None else ""}{"&ig_f="+ig_f if ig_f is not None else ""}{"&ytc_v="+ytc_v if ytc_v is not None else ""}{"&ytc_s="+ytc_s if ytc_s is not None else ""}{"&ytd_vv="+ytd_vv if ytd_vv is not None else ""}{"&ytm_vv="+ytm_vv if ytm_vv is not None else ""}{"&wp_v="+wp_v if wp_v is not None else ""}{"&sc_f="+sc_f if sc_f is not None else ""}{"&bit_f="+bit_f if bit_f is not None else ""}{"&cpp="+cpp if bit_f is not None else ""}{"&t_f="+t_f if t_f is not None else ""}{"&t_v="+t_v if t_v is not None else ""}{"&t_mvh="+t_mvh if t_mvh is not None else ""}{"&t_wvh="+t_wvh if t_wvh is not None else ""}{"&p_ml="+p_ml if p_ml is not None else ""}{"&p_s="+p_s if p_s is not None else ""}{"&p_ls="+p_ls if p_ls is not None else ""}{"&p_lsr="+p_lsr if p_lsr is not None else ""}{"&bp_c="+bp_c if bp_c is not None else ""}{"&bp_f="+bp_f if bp_f is not None else ""}{"&bp_p="+bp_p if bp_p is not None else ""}{"&bp_s="+bp_s if bp_s is not None else ""}{"&career_stage="+career_stage if career_stage is not None else ""}{"&career_stage_score="+career_stage_score if career_stage_score is not None else ""}{"&career_trend="+career_trend if career_trend is not None else ""}{"&career_trend_score="+career_trend_score if career_trend_score is not None else ""}{"&limit="+limit if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}',headers=self.headers)
    #        getArtistsWFResponse.raise_for_status()
    #        return getArtistsWFResponse.json()
    #    except Exception or requests.HTTPError as e:
    #        print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get Artists
    def getArtists(self, platform:str, min:int, max:int, code2:str, genreId:int, subGenreId:int, city:str, unsigned:bool=None, limit:int=None, offset:int=None):
        try:
            getArtistsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{platform}/list?min={min}&max={max}&code2={code2}&genreId={genreId}&subGenreId={subGenreId}&city={city}{"&unsigned="+unsigned if unsigned is not None else ""}{"&limit="+limit if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}',headers=self.headers)
            getArtistsResponse.raise_for_status()
            return getArtistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Historical Artist Rank
    def getArtistsHAR(self, id:int, metric:str=None, date:str=None):
        try:
            getArtistsHARResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/past-artist-rank{"?" if (metric is not None or date is not None) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None and date is not None) else ""}{"date="+date if date is not None else ""}',headers=self.headers)
            getArtistsHARResponse.raise_for_status()
            return getArtistsHARResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Instagram Audience Data Dates
    def getArtistsIGAudienceDates(self, id:int):
        try:
            getArtistsIGAudienceDatesResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/instagram-audience-stats/dates',headers=self.headers)
            getArtistsIGAudienceDatesResponse.raise_for_status()
            return getArtistsIGAudienceDatesResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Instagram Audience Data 
    def getArtistsIGAudienceData(self, id:int, date:str=None, geoOnly:bool=None):
        try:
            getArtistsIGAudienceDataResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/instagram-audience-stats{"?" if (date is not None or geoOnly is not False) else ""}{"date="+date if date is not None else ""}{"&" if (date is not None and geoOnly is not False) else ""}{"geoOnly=true" if geoOnly is not False else ""}',headers=self.headers)
            getArtistsIGAudienceDataResponse.raise_for_status()
            return getArtistsIGAudienceDataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Artist Metadata
    def getArtistsMetadata(self, id:int):
        try:
            getArtistsMetadataResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}',headers=self.headers)
            getArtistsMetadataResponse.raise_for_status()
            return getArtistsMetadataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Neighbouring Artists
    def getArtistsNeighbors(self, id:int, metric:str=None, limit:int=None, genreType:str=None):
        try:
            getArtistsNeighborsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/neighboring-artists{"?" if (metric is not None or limit is not None or genreType is not None) else ""}{"metric="+metric if metric is not None else ""}{"&" if (metric is not None and limit is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if ((limit is not None or metric is not None) and genreType is not None) else ""}{"type="+str(genreType) if genreType is not None else ""}',headers=self.headers)
            getArtistsNeighborsResponse.raise_for_status()
            return getArtistsNeighborsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)  
    
        #Artist Playlists
    def getArtistsPlaylists(self, id, platform, status, since=None, until=None, indie=None, editorial=None, majorCurator=None, limit=None, offset=None):
        try:
            getArtistsPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/{platform}/{status}/playlists{"?" if (since is not None or until is not None or indie is not None or editorial is not None or majorCurator is not None or limit is not None or offset) else ""}{"since="+since if since is not None else ""}',headers=self.headers)
            getArtistsPlaylistsResponse.raise_for_status()
            return getArtistsPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__) 
    
        #Artist Related Artists
    def getArtistsRelatedArtists(self, id:int, limit:int=None, fromDaysAgo:int=None, toDaysAgo:int=None):
        try:
            getArtistsRelatedArtistsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/relatedartists{"?" if (limit is not None or fromDaysAgo is not None or toDaysAgo is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if limit is not None and fromDaysAgo is not None else ""}{"fromDaysAgo="+str(fromDaysAgo) if fromDaysAgo is not None else ""}{"&" if (fromDaysAgo is not None or limit is not None) and toDaysAgo is not None else ""}{"toDaysAgo="+str(toDaysAgo) if toDaysAgo is not None else ""}',headers=self.headers)
            getArtistsRelatedArtistsResponse.raise_for_status()
            return getArtistsRelatedArtistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Artist Social / Streaming Service URLs
    def getArtistSocials(self,id:int):
        try:
            getArtistSocialsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/urls',headers=self.headers)
            getArtistSocialsResponse.raise_for_status()
            return getArtistSocialsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
    
        #Artist Social Audience Stats
    def getArtistSocialAudienceStats(self,id:int, audienceType:str, statsType:str, domain:str, since:str=None, until:str=None, offset:int=None, limit:int=None):
        try:
            getArtistSocialAudienceStatsResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/social-audience-stats?domain={domain}&audienceType={audienceType}&statsType={statsType}{"&since="+since if since is not None else ""}{"&until="+until if until is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&limit="+str(limit) if limit is not None else ""}',headers=self.headers)
            getArtistSocialAudienceStatsResponse.raise_for_status()
            return getArtistSocialAudienceStatsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Spotify Monthly Listeners by City
    def getArtistSpotifyMLbyCity(self,id:int, since:str, until:str=None, latest:bool=None, showHistory:bool=None, offset:int=None, limit:int=None):
        try:
            getArtistSpotifyMLbyCityResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/where-people-listen?since={since}{"&until="+str(until) if until is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}{"&showHistory=true" if showHistory is not False else ""}',headers=self.headers)
            getArtistSpotifyMLbyCityResponse.raise_for_status()
            return getArtistSpotifyMLbyCityResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist TV Show Appearances
    def getArtistTVShowAppearances(self,id:int):
        try:
            getArtistTVShowAppearancesResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tvmaze',headers=self.headers)
            getArtistTVShowAppearancesResponse.raise_for_status()
            return getArtistTVShowAppearancesResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Tiktok Audience Data
    def getArtistTiktokAudienceData(self,id:int, date:str=None):
        try:
            getArtistTiktokAudienceDataResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tiktok-audience-stats{"?date="+date if date is not None else ""}',headers=self.headers)
            getArtistTiktokAudienceDataResponse.raise_for_status()
            return getArtistTiktokAudienceDataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Top Tracks by Platform
    def getArtistTopTracks(self, id:int, source:str, limit:int=None):
        try:
            getArtistTopTracksResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/top-tracks/{source}{"?limit="+str(limit) if limit is not None else ""}',headers=self.headers)
            getArtistTopTracksResponse.raise_for_status()
            return getArtistTopTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Tracks
    def getArtistTracks(self,id, offset=None, limit=None, artistType=None):
        try:
            getArtistTracksResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/tracks{"?" if offset is not None or limit is not None or artistType is not None else ""}{"offset="+str(offset) if offset is not None else ""}{"&" if offset is not None and limit is not None else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if (limit is not None or offset is not None) and artistType is not None else ""}{"artist_type="+artistType if artistType is not None else ""}',headers=self.headers)
            getArtistTracksResponse.raise_for_status()
            return getArtistTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Artist Youtube Audience Data
    def getArtistYoutubeAudience(self,id, date=None, geoOnly=None):
        try:
            getArtistYoutubeAudienceResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/youtube-audience-stats{"?" if date is not None or geoOnly is not False else ""}{"date="+date if date is not None else ""}{"&" if date is not None and geoOnly is not False else ""}{"geoOnly=true" if geoOnly is not False else ""}',headers=self.headers)
            getArtistYoutubeAudienceResponse.raise_for_status()
            return getArtistYoutubeAudienceResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Artist Youtube Views and Market Coverage
    def getArtistYoutubeViewsAndCoverage(self,id):
        try:
            getArtistYoutubeViewsAndCoverageResponse=self.session.get(f'https://api.chartmetric.com/api/artist/{id if isinstance(id, str) else str(id)}/market-coverage-views/youtube',headers=self.headers)
            getArtistYoutubeViewsAndCoverageResponse.raise_for_status()
            return getArtistYoutubeViewsAndCoverageResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #BRAND
        #Brand Info
    def getBrandInfo(self, id:int, sortColumn:str=None, sortOrderDesc:bool=False, limit:int=None, offset:int=None):
        try:
            getBrandInfoResponse=self.session.get(f'https://api.chartmetric.com/api/brand/{id if isinstance(id, str) else str(id)}{"?" if sortColumn is not None or sortOrderDesc is not False or limit is not None or offset is not None else ""}{"sortColumn="+sortColumn if sortColumn is not None else ""}{"&" if sortColumn is not None and (sortOrderDesc is not False or limit is not None or offset is not None) else ""}{"sortOrderDesc=true" if sortOrderDesc is not False else ""}{"&" if sortOrderDesc is not False and (limit is not None or offset is not None) else ""}{"limit="+str(limit) if limit is not None else ""}{"&" if limit is not None and offset is not None else ""}{"offset="+str(offset) if offset is not None else ""}',headers=self.headers)
            getBrandInfoResponse.raise_for_status()
            return getBrandInfoResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Brand List by Interest
    def getBrandListbyInterest(self, sortColumn:str=None):
        try:
            getBrandListbyInterestResponse=self.session.get(f'https://api.chartmetric.com/api/brand/list/by/interest{"?sortColumn="+sortColumn if sortColumn is not None else ""}',headers=self.headers)
            getBrandListbyInterestResponse.raise_for_status()
            return getBrandListbyInterestResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Brand List
    def getBrandList(self):
        try:
            getBrandListResponse=self.session.get(f'https://api.chartmetric.com/api/brand/list',headers=self.headers)
            getBrandListResponse.raise_for_status()
            return getBrandListResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #CHARTS

        #Charts Airplay
    def getChartsAirplay(self, chart_type:str, date:str, since:str, limit:int, duration:str, country_code:str=None, latest:bool=None):
        try:
            getChartsAirplayResponse=self.session.get(f'https://api.chartmetric.com/api/charts/airplay/{chart_type}?date={date}&since={since}&limit={limit}&duration={duration}{"&country_code="+country_code if country_code is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsAirplayResponse.raise_for_status()
            return getChartsAirplayResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
    
        #Charts Amazon
    def getChartsAmazon(self, chart_type:str, sub_type:str, date:str, genre:str, code2:str=None, offset:int=None, latest:bool=False):
        try:
            genre="+".join(genre.split(" "))
            getChartsAmazonResponse=self.session.get(f'https://api.chartmetric.com/api/charts/amazon/{chart_type}?type={sub_type}&date={date}&genre={genre}{"&code2="+code2 if code2 is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsAmazonResponse.raise_for_status()
            return getChartsAmazonResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Apple Music
    def getChartsAppleMusic(self, chart_type:str, sub_type:str, date:str, code2:str, city_id:int=None, genre:str=None, offset:int=None, latest:bool=False):
        try:
            genre="+".join(genre.split(" "))
            getChartsAppleMusicResponse=self.session.get(f'https://api.chartmetric.com/api/charts/applemusic/{chart_type}?type={sub_type}&date={date}&country_code={code2}{"&city_id="+str(city_id) if city_id is not None else ""}{"&genre="+genre if genre is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsAppleMusicResponse.raise_for_status()
            return getChartsAppleMusicResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Beatport
    def getChartsBeatport(self, date:str, genre:str, offset:int=None, latest:bool=False):
        try:
            getChartsBeatportResponse=self.session.get(f'https://api.chartmetric.com/api/charts/beatport?date={date}&genre={genre}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsBeatportResponse.raise_for_status()
            return getChartsBeatportResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Countries
    def getChartsCountries(self, platform:str, chart_type:str, sub_type:str, duration:str):
        try:
            getChartsCountriesResponse=self.session.get(f'https://api.chartmetric.com/api/charts/{platform}/countries?chart_type={chart_type}&type={sub_type}&duration={duration}',headers=self.headers)
            getChartsCountriesResponse.raise_for_status()
            return getChartsCountriesResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Charts Chartmetric Score
    def getChartsChartmetricScore(self, asset_type:str, type_id:int, chart_type:str, since:str, until:str=None):
        try:
            getChartsChartmetricScoreResponse=self.session.get(f'https://api.chartmetric.com/api/charts/{asset_type}/{type_id}/{chart_type}/cm-score?since={since}{"&until="+until if until is not None else ""}',headers=self.headers)
            getChartsChartmetricScoreResponse.raise_for_status()
            return getChartsChartmetricScoreResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Charts Deezer
    def getChartsDeezer(self, country_code:str, date:str, latest:bool=False):
        try:
            getChartsDeezerResponse=self.session.get(f'https://api.chartmetric.com/api/charts/deezer?country_code={country_code}&date={date}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsDeezerResponse.raise_for_status()
            return getChartsDeezerResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts QQ Music
    def getChartsQQMusic(self, date:str, latest:bool=False):
        try:
            getChartsQQMusicResponse=self.session.get(f'https://api.chartmetric.com/api/charts/qq?date={date}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsQQMusicResponse.raise_for_status()
            return getChartsQQMusicResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Shazam (Cities)
    def getChartsShazamCities(self, country_code:str):
        try:
            getChartsQQMusicResponse=self.session.get(f'https://api.chartmetric.com/api/charts/shazam/{country_code}/cities',headers=self.headers)
            getChartsQQMusicResponse.raise_for_status()
            return getChartsQQMusicResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Shazam 
    def getChartsShazam(self, country_code:str, date:str, city:str=None, offest:int=None, latest:bool=False):
        try:
            getChartsShazamResponse=self.session.get(f'https://api.chartmetric.com/api/charts/shazam?date={date}&country_code={country_code}{"&city="+urllib.parse.quote(city) if city is not None else ""}{"&offset="+str(offest) if offest is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsShazamResponse.raise_for_status()
            return getChartsShazamResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts SoundCloud 
    def getChartsSoundCloud(self, country_code:str, date:str, kind:str, genre:str, offest:int=None, raw:bool=False, latest:bool=False):
        try:
            getChartsSoundCloudResponse=self.session.get(f'https://api.chartmetric.com/api/charts/soundcloud?date={date}&country_code={country_code}&kind={kind}&genre={genre}{"&offset="+str(offest) if offest is not None else ""}{"&raw=true" if raw is not False else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsSoundCloudResponse.raise_for_status()
            return getChartsSoundCloudResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Spotify (Artists) 
    def getChartsSpotifyArtists(self, date:str, chart_type:str, interval:str, offest:int=None, latest:bool=False):
        try:
            getChartsSpotifyArtistsResponse=self.session.get(f'https://api.chartmetric.com/api/charts/spotify/artists?date={date}&interval={interval}&type={chart_type}{"&offset="+str(offest) if offest is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsSpotifyArtistsResponse.raise_for_status()
            return getChartsSpotifyArtistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Spotify (Freshfind) 
    def getChartsSpotifyFreshfind(self, date:str, latest:bool=False):
        try:
            getChartsSpotifyFreshfindResponse=self.session.get(f'https://api.chartmetric.com/api/charts/spotify/freshfind?date={date}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsSpotifyFreshfindResponse.raise_for_status()
            return getChartsSpotifyFreshfindResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Spotify (Tracks) 
    def getChartsSpotifyTracks(self, date:str, country_code:str, chart_type:str, interval:str, offset:int=None, latest:bool=False):
        try:
            getChartsSpotifyTracksResponse=self.session.get(f'https://api.chartmetric.com/api/charts/spotify?date={date}&country_code={country_code}&interval={interval}&type={chart_type}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsSpotifyTracksResponse.raise_for_status()
            return getChartsSpotifyTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Tiktok Top Tracks Stats (Freq Update)
    def getChartsTiktokTopTracksStats(self, date:str, limit:int=None, offset:int=None):
        try:
            getChartsTiktokTopTracksStatsResponse=self.session.get(f'https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date={date}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}',headers=self.headers)
            getChartsTiktokTopTracksStatsResponse.raise_for_status()
            return getChartsTiktokTopTracksStatsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Charts Tiktok 
    def getChartsTiktok(self, chart_type:str, date:str, user_chart_type:str, interval:str=None, limit:int=None, offset:int=None, latest:bool=False, countryChart:str=False, code2:str=None):
        try:
            getChartsTiktokResponse=self.session.get(f'https://api.chartmetric.com/api/charts/tiktok/{chart_type}?date={date}{"&type="+user_chart_type if chart_type=="users" else ""}{"&interval="+interval if interval is not None else ""}{"&limit="+str(limit) if limit is not None else ""}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}{"&countryChart=true" if countryChart is not False else ""}{"&code2="+code2 if (countryChart is not False) and (code2 is not None) else ""}',headers=self.headers)
            getChartsTiktokResponse.raise_for_status()
            return getChartsTiktokResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Twitch
    def getChartsTwitch(self, since:str, limit:int, duration:str, chart_type:str, date:str=None, latest:bool=False):
        try:
            getChartsTwitchResponse=self.session.get(f'https://api.chartmetric.com/api/charts/twitch/users?since={since}&type={chart_type}&duration={duration}&limit={limit}{"&date="+date if date is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsTwitchResponse.raise_for_status()
            return getChartsTwitchResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts Youtube
    def getChartsYoutube(self, chart_type:str, country_code:str, date:str, offset:int=None, latest:bool=False):
        try:
            getChartsYoutubeResponse=self.session.get(f'https://api.chartmetric.com/api/charts/youtube/{chart_type}?date={date}&country_code={country_code}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsYoutubeResponse.raise_for_status()
            return getChartsYoutubeResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Charts iTunes 
    def getChartsiTunes(self, chart_type:str, country_code:str, date:str, genre:str, offset:int=None, latest:bool=False):
        try:
            getChartsiTunesResponse=self.session.get(f'https://api.chartmetric.com/api/charts/itunes/{chart_type}?date={date}&country_code={country_code}&genre={genre}{"&offset="+str(offset) if offset is not None else ""}{"&latest=true" if latest is not False else ""}',headers=self.headers)
            getChartsiTunesResponse.raise_for_status()
            return getChartsiTunesResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #CITY

        #Top Artists
    def getCityTopArtists(self, id, source):
        try:
            getCityTopArtistsResponse=self.session.get(f'https://api.chartmetric.com/api/city/{id}/{source}/top-artists',headers=self.headers)
            getCityTopArtistsResponse.raise_for_status()
            return getCityTopArtistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Top Tracks
    def getCityTopTracks(self, id, source):
        try:
            getCityTopTracksResponse=self.session.get(f'https://api.chartmetric.com/api/city/{id}/{source}/top-tracks',headers=self.headers)
            getCityTopTracksResponse.raise_for_status()
            return getCityTopTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #CURATOR

        #Curator List
    def getCuratorList(self, platform, offset=None, limit=None, editorial=None, majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None):
        try:
            getCuratorListResponse=self.session.get(f'https://api.chartmetric.com/api/curator/{platform}/lists',headers=self.headers)
            getCuratorListResponse.raise_for_status()
            return getCuratorListResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Curator Fan Metrics
    def getCuratorFanMetrics(self, id, platform, source, since=None, until=None, field=None, latest=None, interpolated=None):
        try:
            getCuratorFanMetricsResponse=self.session.get(f'https://api.chartmetric.com/api/curator/{platform}/{id}/stat/{source}',headers=self.headers)
            getCuratorFanMetricsResponse.raise_for_status()
            return getCuratorFanMetricsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Curator Metadata
    def getCuratorMetadata(self, id, platform):
        try:
            getCuratorMetadataResponse=self.session.get(f'https://api.chartmetric.com/api/curator/{platform}/{id}/',headers=self.headers)
            getCuratorMetadataResponse.raise_for_status()
            return getCuratorMetadataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Curator Playlists
    def getCuratorPlaylists(self, id, platform, limit=None, offset=None):
        try:    
            getCuratorPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/curator/{platform}/{id}/playlists',headers=self.headers)
            getCuratorPlaylistsResponse.raise_for_status()
            return getCuratorPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Curator Social / Streaming Service URLs
    def getCuratorSocialStreamingURLs(self, id, platform):
        try:
            getCuratorSocialStreamingURLsResponse=self.session.get(f'https://api.chartmetric.com/api/curator/{platform}/{id}/urls',headers=self.headers)
            getCuratorSocialStreamingURLsResponse.raise_for_status()
            return getCuratorSocialStreamingURLsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #PLAYLIST
    
        #Playlist Metadata
    def getPlaylistMetadata(self, id, platform, storefront=None):
        try:
            getPlaylistMetadataResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}',headers=self.headers)
            getPlaylistMetadataResponse.raise_for_status()
            return getPlaylistMetadataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist Evolution Stats (given Artist, Album or Track Chartmetric ID)
    def getPlaylistEvolutionStats(self, type, id, since=None, until=None):
        try:
            getPlaylistEvolutionStatsResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/by/{type}/{id}/evolution',headers=self.headers)
            getPlaylistEvolutionStatsResponse.raise_for_status()
            return getPlaylistEvolutionStatsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist Journey or Progression
    def getPlaylistJourneyProgression(self, platform, type, id, sortColumn=None, sortOrderDesc=None, limit=None, offset=None):
        try:
            getPlaylistJourneyProgressionResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/journey-progression/{type}',headers=self.headers)
            getPlaylistJourneyProgressionResponse.raise_for_status()
            return getPlaylistJourneyProgressionResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist Last Updated Time
    def getPlaylistLastUpdatedTime(self, platform, id, storefron=None):
        try:
            getPlaylistLastUpdatedTimeResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/updated',headers=self.headers)
            getPlaylistLastUpdatedTimeResponse.raise_for_status()
            return getPlaylistLastUpdatedTimeResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist List
    def getPlaylistList(self, platform, sortColumn=None, sortOrderDesc=None, code2=None, tagIds=None, curatorIds=None, limit=None, offset=None, indie=None, majorCurator=None, editorial=None, newMusicFriday=None):
        try:
            getPlaylistListResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/lists?limit=100&offset=9900&sortColumn=followers',headers=self.headers)
            getPlaylistListResponse.raise_for_status()
            return getPlaylistListResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)
        
        #Playlist Snapshot
    def getPlaylistSnapshot(self, id, platform, date, storefront=None):
        try:
            getPlaylistSnapshotResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/snapshot?date={date}',headers=self.headers)
            getPlaylistSnapshotResponse.raise_for_status()
            return getPlaylistSnapshotResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist Stats Over Time
    def getPlaylistStatsOverTime(self, id, platform, since, until=None):
        try:
            getPlaylistStatsOverTimeResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/stats?since={since}',headers=self.headers)
            getPlaylistStatsOverTimeResponse.raise_for_status()
            return getPlaylistStatsOverTimeResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Playlist Tracks (Current, Past)
    def getPlaylistTracks(self, id, platform, span, storefront=None, offset=None, withDetails=None, since=None, until=None):
        try:
            getPlaylistTracksResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/{span}/tracks',headers=self.headers)
            getPlaylistTracksResponse.raise_for_status()
            return getPlaylistTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #RADIO
    
        #Radio Airplay information in Time Series
    def getRadioAirplayInfoinTime(self, id, type, since):
        try:
            getRadioAirplayInfoinTimeResponse=self.session.get(f'https://api.chartmetric.com/api/radio/{type}/{id}/airplays?since={since}',headers=self.headers)
            getRadioAirplayInfoinTimeResponse.raise_for_status()
            return getRadioAirplayInfoinTimeResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Radio Broadcast Market play counts
    def getRadioBroadcastPlayCounts(self, id, type, since):
        try:
            getRadioBroadcastPlayCountsResponse=self.session.get(f'https://api.chartmetric.com/api/radio/{type}/{id}/broadcast-markets?since={since}',headers=self.headers)
            getRadioBroadcastPlayCountsResponse.raise_for_status()
            return getRadioBroadcastPlayCountsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get Radio Station List for Country
    def getRadioStationList(self, code2=None):
        try:
            getRadioStationListResponse=self.session.get(f'https://api.chartmetric.com/api/radio/station-list?code2={code2}',headers=self.headers)
            getRadioStationListResponse.raise_for_status()
            return getRadioStationListResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Radio Total Airplays
    def getRadioTotalAirplay(self, id, type, since, limit=None):
        try:
            getRadioTotalAirplayResponse=self.session.get(f'https://api.chartmetric.com/api/radio/{type}/{id}/airplay-totals?limit={limit}&since={since}',headers=self.headers)
            getRadioTotalAirplayResponse.raise_for_status()
            return getRadioTotalAirplayResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #RECOMMENDATION

        #Get 100 Similar Playlists
    def getRecommendationSimilarPlaylists(self, id, platform, storefront=None, indie=None, limit=None):
        try:
            getRecommendationSimilarPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/playlist/{platform}/{id}/similarplaylists',headers=self.headers)
            getRecommendationSimilarPlaylistsResponse.raise_for_status()
            return getRecommendationSimilarPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #SEARCH

        #Chartmetric Search Engine
    def search(self, q, limit=None, offset=None, type=None):
        try:
            searchResponse=self.session.get(f'https://api.chartmetric.com/api/search?q={q}',headers=self.headers)
            searchResponse.raise_for_status()
            return searchResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get City Info
    def getCityInfo(self, country_code):
        try:
            getCityInfoResponse=self.session.get(f'https://api.chartmetric.com/api/cities?country_code={country_code}',headers=self.headers)
            getCityInfoResponse.raise_for_status()
            return getCityInfoResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Get Genre Ids
    def getGenreIds(self, name=None):
        try:
            getGenreIdsResponse=self.session.get(f'https://api.chartmetric.com/api/genres?name={name}',headers=self.headers)
            getGenreIdsResponse.raise_for_status()
            return getGenreIdsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

    #TRACK 

        #Track Charts
    def getTrackCharts(self, type, id, since, until=None):
        try:
            getTrackChartsResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/{type}/charts?since={since}',headers=self.headers)
            getTrackChartsResponse.raise_for_status()
            return getTrackChartsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Get Track IDs
    def getTrackIDs(self, type, id):
        try:
            getTrackIDsResponse=self.session.get(f'https://api.chartmetric.com/api/track/{type}/{id}/get-ids',headers=self.headers)
            getTrackIDsResponse.raise_for_status()
            return getTrackIDsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Get Tracks (with filters)
    def getTracksWFilter(self, limit=None,offset=None,sortOrderDesc=None,sortColumn=None,genres=None,artists=None,range_period=None,max_score=None,min_score=None,max_release_date=None,min_release_date=None,max_airplay_streams=None,min_airplay_streams=None,max_amazon_playlist_count=None,min_amazon_playlist_count=None,max_deezer_playlist_count=None,min_deezer_playlist_count=None,max_itunes_playlist_count=None,min_itunes_playlist_count=None,max_shazam_count=None,min_shazam_count=None,max_siriusxm_streams=None,min_siriusxm_streams=None,max_soundcloud_plays=None,min_soundcloud_plays=None,max_spotify_playlist_count=None,min_spotify_playlist_count=None,max_spotify_plays=None,min_spotify_plays=None,max_spotify_popularity=None,min_spotify_popularity=None,max_tiktok_posts=None,min_tiktok_posts=None,max_tiktok_top_videos_likes=None,min_tiktok_top_videos_likes=None,max_tiktok_top_videos_views=None,min_tiktok_top_videos_views=None,max_youtube_likes=None,min_youtube_likes=None,max_youtube_playlist_count=None,min_youtube_playlist_count=None):
        try:
            getTracksWFilterResponse=self.session.get(f'https://api.chartmetric.com/api/track/list/filter',headers=self.headers)
            getTracksWFilterResponse.raise_for_status()
            return getTracksWFilterResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Get Metadata
    def getTrackMetadata(self, id):
        try:
            getTrackMetadataResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}',headers=self.headers)
            getTrackMetadataResponse.raise_for_status()
            return getTrackMetadataResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Playlist Snapshot
    def getTrackPlaylistSnapshot(self, id,platform,storefront=None,limit=None,offset=None):
        try:
            getTrackPlaylistSnapshotResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/{platform}/playlists/snapshot',headers=self.headers)
            getTrackPlaylistSnapshotResponse.raise_for_status()
            return getTrackPlaylistSnapshotResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Playlist 
    def getTrackPlaylists(self, id,platform,status,since=None,until=None,indie=None,limit=None,offset=None,sortColumn=None,editorial=None,majorCurator=None):
        try:
            getTrackPlaylistsResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/{platform}/{status}/playlists',headers=self.headers)
            getTrackPlaylistsResponse.raise_for_status()
            return getTrackPlaylistsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Related Tracks 
    def getTrackRelatedTracks(self, id):
        try:
            getTrackRelatedTracksResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/relatedTracks',headers=self.headers)
            getTrackRelatedTracksResponse.raise_for_status()
            return getTrackRelatedTracksResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Stats 
    def getTrackStats(self, id,platform,mode,since=None,until=None,latest=None,interpolated=None,type=None,isDomainId=None):
        try:
            getTrackStatsResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/{platform}/stats/{mode}',headers=self.headers)
            getTrackStatsResponse.raise_for_status()
            return getTrackStatsResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)

        #Track Top TikTok Video 
    def getTrackTopTikTokVideo(self, id, limit=None,type=None):
        try:
            getTrackTopTikTokVideoResponse=self.session.get(f'https://api.chartmetric.com/api/track/{id}/topVideos',headers=self.headers)
            getTrackTopTikTokVideoResponse.raise_for_status()
            return getTrackTopTikTokVideoResponse.json()
        except Exception or requests.HTTPError as e:
            print(str(e) if type(e)==requests.HTTPError else e.__str__)