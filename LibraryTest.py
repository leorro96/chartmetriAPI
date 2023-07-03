import unittest
from APICaller_copy import APICaller

caller=APICaller("hfvRknFEugQIkaLhZ5Ko1GVvgNEG3eznqccvrFJDA6pePlT5lLYHeABuVVfrRUQr")
class TestAPICaller(unittest.TestCase):
    #ALBUM
        #Charts
    def test_getAlbumCharts(self):
        self.assertEqual(caller.getAlbumCharts("applemusic",3533190),"https://api.chartmetric.com/api/album/3533190/applemusic/charts")
        self.assertEqual(caller.getAlbumCharts("applemusic",3533190,since="2020-03-01"),"https://api.chartmetric.com/api/album/3533190/applemusic/charts?since=2020-03-01")
        self.assertEqual(caller.getAlbumCharts("applemusic",3533190,until="2020-03-04"),"https://api.chartmetric.com/api/album/3533190/applemusic/charts?until=2020-03-04")
        self.assertEqual(caller.getAlbumCharts("applemusic",3533190,since="2020-03-01",until="2020-03-04"),"https://api.chartmetric.com/api/album/3533190/applemusic/charts?since=2020-03-01&until=2020-03-04")    
        #IDs
    def test_getAlbumIDs(self):
        self.assertEqual(caller.getAlbumIDs("chartmetric",815685),"https://api.chartmetric.com/api/album/chartmetric/815685/get-ids")        
        #Metadata
    def test_getAlbumMetadata(self):
        self.assertEqual(caller.getAlbumMetadata(815685),"https://api.chartmetric.com/api/album/815685")        
        #Playlists        
    def test_getAlbumPlaylists(self):
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20"),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20", offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20"),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",limit=100, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&limit=100&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",limit=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&limit=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",indie=True, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&indie=true&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",indie=True),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&indie=true")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",indie=True,limit=100, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&indie=true&limit=100&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", until="2020-09-20",indie=True,limit=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&until=2020-09-20&indie=true&limit=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20", offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20"),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",limit=100, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&limit=100&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",limit=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&limit=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",indie=True, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&indie=true&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",indie=True),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&indie=true")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",indie=True,limit=100, offset=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&indie=true&limit=100&offset=100")        
        self.assertEqual(caller.getAlbumPlaylists(5449730, "spotify", "current", "2020-09-20",indie=True,limit=100),"https://api.chartmetric.com/api/album/5449730/spotify/current/playlists?since=2020-09-20&indie=true&limit=100")        
        #Stats    
    def test_getAlbumStats(self):
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers"),"https://api.chartmetric.com/api/album/6382276/spotify/followers")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers", latest=True),"https://api.chartmetric.com/api/album/6382276/spotify/followers?latest=true")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers", until="2020-09-23"),"https://api.chartmetric.com/api/album/6382276/spotify/followers?until=2020-09-23")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers", until="2020-09-23", latest=True),"https://api.chartmetric.com/api/album/6382276/spotify/followers?until=2020-09-23&latest=true")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers",since="2020-09-20"),"https://api.chartmetric.com/api/album/6382276/spotify/followers?since=2020-09-20")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers",since="2020-09-20", latest=True),"https://api.chartmetric.com/api/album/6382276/spotify/followers?since=2020-09-20&latest=true")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers",since="2020-09-20", until="2020-09-23"),"https://api.chartmetric.com/api/album/6382276/spotify/followers?since=2020-09-20&until=2020-09-23")
        self.assertEqual(caller.getAlbumStats(6382276, "spotify", "followers",since="2020-09-20", until="2020-09-23", latest=True),"https://api.chartmetric.com/api/album/6382276/spotify/followers?since=2020-09-20&until=2020-09-23&latest=true")
        #Tracks            
    def test_getAlbumTracks(self):
        self.assertEqual(caller.getAlbumTracks(3533190),"https://api.chartmetric.com/api/album/3533190/tracks")


    #ARTIST
        #ANR - By Social Index
    def test_getArtistANRbySI(self):
        self.assertEqual(caller.getArtistANRbySI("spotify_monthly_listeners"),"https://api.chartmetric.com/api/artist/anr/by/social-index?sortBy=spotify_monthly_listeners")
        self.assertEqual(caller.getArtistANRbySI("spotify_monthly_listeners",offset=100, limit=100, tagIds=1234, subTagIds=1234, maxSpotifyFollowers=100, sortOrderDesc=True, recentReleaseWithin=100,latestReleaseWithin=100),"https://api.chartmetric.com/api/artist/anr/by/social-index?sortBy=spotify_monthly_listeners&offset=100&limit=100&tagIds=1234&subTagIds=1234&maxSpotifyFollowers=100&sortOrderDesc=true&recentReleaseWithin=100&latestReleaseWithin=100")
              
        #ANR - By Playlists
    def test_getArtistANRbyPlaylists(self):
        self.assertEqual(caller.getArtistANRbyPlaylists(sortBy="followers_total_reach_diff_week", streamingType="spotify", limit=100),"https://api.chartmetric.com/api/artist/anr/by/playlists?sortBy=followers_total_reach_diff_week&streamingType=spotify&limit=100")

        #Albums
    def test_getArtistAlbums(self):
        self.assertEqual(caller.getArtistAlbums("3380"),"https://api.chartmetric.com/api/artist/3380/albums")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date"),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date")
        self.assertEqual(caller.getArtistAlbums("3380", sortOrderDesc=True),"https://api.chartmetric.com/api/artist/3380/albums?sortOrderDesc=true")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date", sortOrderDesc=True),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&sortOrderDesc=true")
        self.assertEqual(caller.getArtistAlbums("3380", offset=100),"https://api.chartmetric.com/api/artist/3380/albums?offset=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date", offset=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&offset=100")
        self.assertEqual(caller.getArtistAlbums("3380",sortOrderDesc=True, offset=100),"https://api.chartmetric.com/api/artist/3380/albums?sortOrderDesc=true&offset=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date",sortOrderDesc=True, offset=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&sortOrderDesc=true&offset=100")
        self.assertEqual(caller.getArtistAlbums("3380",limit=100),"https://api.chartmetric.com/api/artist/3380/albums?limit=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date",limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380",sortOrderDesc=True,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortOrderDesc=true&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date",sortOrderDesc=True,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&sortOrderDesc=true&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380", offset=100,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?offset=100&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date", offset=100,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&offset=100&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380",sortOrderDesc=True, offset=100,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortOrderDesc=true&offset=100&limit=100")
        self.assertEqual(caller.getArtistAlbums("3380", sortColumn="release_date",sortOrderDesc=True, offset=100,limit=100),"https://api.chartmetric.com/api/artist/3380/albums?sortColumn=release_date&sortOrderDesc=true&offset=100&limit=100")
        #Rank
    def test_getArtistRank(self):
        self.assertEqual(caller.getArtistRank("3380"),"https://api.chartmetric.com/api/artist/3380/artist-rank")
        self.assertEqual(caller.getArtistRank("3380", metric="fs_likes"),"https://api.chartmetric.com/api/artist/3380/artist-rank?metric=fs_likes")
        self.assertEqual(caller.getArtistRank("3380", code2="ES"),"https://api.chartmetric.com/api/artist/3380/artist-rank?code2=ES")
        self.assertEqual(caller.getArtistRank("3380", metric="fs_likes", code2="ES"),"https://api.chartmetric.com/api/artist/3380/artist-rank?metric=fs_likes&code2=ES")
        self.assertEqual(caller.getArtistRank("3380", genre=2),"https://api.chartmetric.com/api/artist/3380/artist-rank?genre=2")
        self.assertEqual(caller.getArtistRank("3380", metric="fs_likes", genre=2),"https://api.chartmetric.com/api/artist/3380/artist-rank?metric=fs_likes&genre=2")
        self.assertEqual(caller.getArtistRank("3380", code2="ES", genre=2),"https://api.chartmetric.com/api/artist/3380/artist-rank?code2=ES&genre=2")
        self.assertEqual(caller.getArtistRank("3380", metric="fs_likes", code2="ES", genre=2),"https://api.chartmetric.com/api/artist/3380/artist-rank?metric=fs_likes&code2=ES&genre=2")

        #CPP (Cross-Platform Performance)
    def test_getArtistCPP(self):
        self.assertEqual(caller.getArtistCPP("3380", stat="rank"),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", since="2019-12-10"),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&since=2019-12-10")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", until="2019-12-10"),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&until=2019-12-10")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", since="2019-12-10", until="2019-12-10"),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&since=2019-12-10&until=2019-12-10")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", latest=True),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&latest=true")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", since="2019-12-10",latest=True),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&since=2019-12-10&latest=true")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", until="2019-12-10",latest=True),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&until=2019-12-10&latest=true")
        self.assertEqual(caller.getArtistCPP("3380", stat="rank", since="2019-12-10", until="2019-12-10",latest=True),"https://api.chartmetric.com/api/artist/3380/cpp?stat=rank&since=2019-12-10&until=2019-12-10&latest=true")
        
        #Career History
    def test_getArtistCareer(self):
        self.assertEqual(caller.getArtistCareer("3380"),"https://api.chartmetric.com/api/artist/3380/career")
        self.assertEqual(caller.getArtistCareer("3380", since="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380", until="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?until=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01", until="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&until=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380", limit=100),"https://api.chartmetric.com/api/artist/3380/career?limit=100")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&limit=100")
        self.assertEqual(caller.getArtistCareer("3380", until="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?until=2022-10-01&limit=100")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01", until="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&until=2022-10-01&limit=100")
        self.assertEqual(caller.getArtistCareer("3380"),"https://api.chartmetric.com/api/artist/3380/career")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380", until="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?until=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01", until="2022-10-01"),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&until=2022-10-01")
        self.assertEqual(caller.getArtistCareer("3380", limit=100),"https://api.chartmetric.com/api/artist/3380/career?limit=100")
        self.assertEqual(caller.getArtistCareer("3380",since="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&limit=100")
        self.assertEqual(caller.getArtistCareer("3380", until="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?until=2022-10-01&limit=100")
        self.assertEqual(caller.getArtistCareer("3380", since="2022-10-01", until="2022-10-01", limit=100),"https://api.chartmetric.com/api/artist/3380/career?since=2022-10-01&until=2022-10-01&limit=100")

        #Charts
    def test_getArtistCharts(self):
        self.assertEqual(caller.getArtistCharts("3380",platform="spotify_top_daily",since="2020-03-01", duration="daily"),"https://api.chartmetric.com/api/artist/3380/spotify_top_daily/charts?since=2020-03-01&duration=daily")
        self.assertEqual(caller.getArtistCharts("3380",platform="spotify_top_daily",since="2020-03-01", duration="daily", until="2020-03-01"),"https://api.chartmetric.com/api/artist/3380/spotify_top_daily/charts?since=2020-03-01&duration=daily&until=2020-03-01")

        #Fan Metrics  
    def test_getFansMetrics(self):
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", field="followers", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?field=followers&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", field="followers", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&field=followers&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", field="followers", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&field=followers&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", field="followers", code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&field=followers&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", field="followers", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?field=followers&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", field="followers", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&field=followers&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", field="followers", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&field=followers&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", field="followers", latest=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&field=followers&latest=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", interpolated=True, isDomainId=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?interpolated=true&isDomainId=true&code2=ES&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", interpolated=True, isDomainId=True, city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&interpolated=true&isDomainId=true&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", interpolated=True, isDomainId=True, city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&interpolated=true&isDomainId=true&city_id=2")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", field="followers", interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?field=followers&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", field="followers", interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&field=followers&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", field="followers", interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&field=followers&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", field="followers", interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&field=followers&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", field="followers", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?field=followers&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", field="followers", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&field=followers&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", until="2017-03-25", field="followers", latest=True, interpolated=True, isDomainId=True),"https://api.chartmetric.com/api/artist/3380/stat/spotify?until=2017-03-25&field=followers&latest=true&interpolated=true&isDomainId=true")
        self.assertEqual(caller.getFansMetrics("3380", source="spotify", since="2017-03-25", until="2017-03-25", field="followers", latest=True, interpolated=True, isDomainId=True, code2="ES", city_id=2),"https://api.chartmetric.com/api/artist/3380/stat/spotify?since=2017-03-25&until=2017-03-25&field=followers&latest=true&interpolated=true&isDomainId=true&code2=ES&city_id=2")
  
        #Get Artist IDs
    def test_getArtistIDs(self):
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, limit=100),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?limit=100")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, offset=1),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?offset=1")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, limit=100, offset=1),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?limit=100&offset=1")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, aggregate=True),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?aggregate=true")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, limit=100, aggregate=True),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?limit=100&aggregate=true")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, offset=1, aggregate=True),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?offset=1&aggregate=true")
        self.assertEqual(caller.getArtistIDs(platform="chartmetric",id=4904, limit=100, offset=1, aggregate=True),"https://api.chartmetric.com/api/artist/chartmetric/4904/get-ids?limit=100&offset=1&aggregate=true")


        #Get Artist RIAA Awards   
    def test_getArtistRIAA(self):
        self.assertEqual(caller.getArtistRIAA(3380),"https://api.chartmetric.com/api/artist/3380/riaa")
  

        #Get Artists (with filters)
#    def test_getArtistsWF(self):
 #       self.assertEqual(caller.getArtistsWF(limit=50,offset=10,sortColumn="cm_artist_rank",code2="US",band=False,cpp=[2,30]),"https://api.chartmetric.com/api/artist/list/filter?limit=50&offset=10&sortColumn=cm_artist_rank&sortOrderDesc=false&code2=US&band=false&cpp=[2,30]")


        #Get Artists
    def test_getArtists(self):
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago"),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago",unsigned=True),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&unsigned=true")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago", limit=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&limit=100")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago",unsigned=True, limit=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&unsigned=true&limit=100")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago", offset=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&offset=100")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago",unsigned=True, offset=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&unsigned=true&offset=100")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago", limit=100, offset=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&limit=100&offset=100")
        self.assertEqual(caller.getArtists(platform="sp_followers", genreId=1, subGenreId=2, min=500, max=10000, code2="US", city="Chicago",unsigned=True, limit=100, offset=100),"https://api.chartmetric.com/api/artist/sp_followers/list?min=500&max=10000&code2=US&genreId=1&subGenreId=2&city=Chicago&unsigned=true&limit=100&offset=100")

        #Historical Artist Rank
    def test_getArtistsHAR(self):
        self.assertEqual(caller.getArtistsHAR(3648),"https://api.chartmetric.com/api/artist/3648/past-artist-rank")
        self.assertEqual(caller.getArtistsHAR(3648, metric="cm_artist_subgenre_rank"),"https://api.chartmetric.com/api/artist/3648/past-artist-rank?metric=cm_artist_subgenre_rank")
        self.assertEqual(caller.getArtistsHAR(3648, date="2021-09-11"),"https://api.chartmetric.com/api/artist/3648/past-artist-rank?date=2021-09-11")
        self.assertEqual(caller.getArtistsHAR(3648, metric="cm_artist_subgenre_rank", date="2021-09-11"),"https://api.chartmetric.com/api/artist/3648/past-artist-rank?metric=cm_artist_subgenre_rank&date=2021-09-11")


        #Instagram Audience Data Dates
    def test_getArtistsIGAudienceDates(self):
        self.assertEqual(caller.getArtistsIGAudienceDates(3648),"https://api.chartmetric.com/api/artist/3648/instagram-audience-stats/dates")

        #Instagram Audience Data 
    def test_getArtistsIGAudienceData(self):
        self.assertEqual(caller.getArtistsIGAudienceData(3648),"https://api.chartmetric.com/api/artist/3648/instagram-audience-stats")
        self.assertEqual(caller.getArtistsIGAudienceData(3648, date="2022-04-03"),"https://api.chartmetric.com/api/artist/3648/instagram-audience-stats?date=2022-04-03")
        self.assertEqual(caller.getArtistsIGAudienceData(3648, geoOnly=True),"https://api.chartmetric.com/api/artist/3648/instagram-audience-stats?geoOnly=true")
        self.assertEqual(caller.getArtistsIGAudienceData(3648, date="2022-04-03", geoOnly=True),"https://api.chartmetric.com/api/artist/3648/instagram-audience-stats?date=2022-04-03&geoOnly=true")

        #Artist Metadata
    def test_getArtistsMetadata(self):
        self.assertEqual(caller.getArtistsMetadata(3648),"https://api.chartmetric.com/api/artist/3648")

        
        #Artist Neighbouring Artists
    def test_getArtistsNeighbors(self):
        self.assertEqual(caller.getArtistsNeighbors(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
        self.assertEqual(caller.getArtistsNeighbors(3648, metric="cm_artist_rank"),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?metric=cm_artist_rank")
        self.assertEqual(caller.getArtistsNeighbors(3648, limit=100),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?limit=100")
        self.assertEqual(caller.getArtistsNeighbors(3648, metric="cm_artist_rank", limit=100),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?metric=cm_artist_rank&limit=100")
        self.assertEqual(caller.getArtistsNeighbors(3648, genreType="Pop"),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?type=Pop")
        self.assertEqual(caller.getArtistsNeighbors(3648, metric="cm_artist_rank", genreType="Pop"),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?metric=cm_artist_rank&type=Pop")
        self.assertEqual(caller.getArtistsNeighbors(3648, limit=100, genreType="Pop"),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?limit=100&type=Pop")
        self.assertEqual(caller.getArtistsNeighbors(3648, metric="cm_artist_rank", limit=100, genreType="Pop"),"https://api.chartmetric.com/api/artist/3648/neighboring-artists?metric=cm_artist_rank&limit=100&type=Pop")

        #Artist Playlists
#    def test_getArtistsPlaylists(self):
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")
#        self.assertEqual(caller.getArtistsPlaylists(3648),"https://api.chartmetric.com/api/artist/3648/neighboring-artists")

    
        #Artist Related Artists
    def test_getArtistsRelatedArtists(self):
        self.assertEqual(caller.getArtistsRelatedArtists(3648),"https://api.chartmetric.com/api/artist/3648/relatedartists")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, limit=100),"https://api.chartmetric.com/api/artist/3648/relatedartists?limit=100")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, fromDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?fromDaysAgo=1")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, limit=100, fromDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?limit=100&fromDaysAgo=1")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, toDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?toDaysAgo=1")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, limit=100, toDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?limit=100&toDaysAgo=1")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, fromDaysAgo=1, toDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?fromDaysAgo=1&toDaysAgo=1")
        self.assertEqual(caller.getArtistsRelatedArtists(3648, limit=100, fromDaysAgo=1, toDaysAgo=1),"https://api.chartmetric.com/api/artist/3648/relatedartists?limit=100&fromDaysAgo=1&toDaysAgo=1")        

        #Artist Social / Streaming Service URLs
    def test_getArtistSocials(self):
        self.assertEqual(caller.getArtistSocials(3648),"https://api.chartmetric.com/api/artist/3648/urls")
        
        #Artist Social Audience Stats
    def test_getArtistSocialAudienceStats(self):
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country"),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25"),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", until="2017-03-25"),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&until=2017-03-25")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", until="2017-03-25"),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&until=2017-03-25")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", offset=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&offset=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", offset=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&offset=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", until="2017-03-25", offset=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&until=2017-03-25&offset=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", until="2017-03-25", offset=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&until=2017-03-25&offset=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", until="2017-03-25", limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&until=2017-03-25&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", until="2017-03-25", limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&until=2017-03-25&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", offset=100, limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&offset=100&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", offset=100, limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&offset=100&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", until="2017-03-25", offset=100, limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&until=2017-03-25&offset=100&limit=100")
        self.assertEqual(caller.getArtistSocialAudienceStats(3963, domain="instagram", audienceType="followers", statsType="country", since="2017-03-25", until="2017-03-25", offset=100, limit=100),"https://api.chartmetric.com/api/artist/3963/social-audience-stats?domain=instagram&audienceType=followers&statsType=country&since=2017-03-25&until=2017-03-25&offset=100&limit=100")
        
        #Artist Spotify Monthly Listeners by City
    def test_getArtistSpotifyMLbyCity(self):
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25"),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25"),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", limit=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&limit=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", limit=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&limit=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", offset=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&offset=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", offset=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&offset=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", limit=100, offset=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&limit=100&offset=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", limit=100, offset=100),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&limit=100&offset=100")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", limit=100, latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&limit=100&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", limit=100, latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&limit=100&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", offset=100, latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&offset=100&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", offset=100, latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&offset=100&latest=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", limit=100, offset=100, latest=True, showHistory=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&limit=100&offset=100&latest=true&showHistory=true")
        self.assertEqual(caller.getArtistSpotifyMLbyCity(3963, since="2017-03-25", until="2017-03-25", limit=100, offset=100, latest=True),"https://api.chartmetric.com/api/artist/3963/where-people-listen?since=2017-03-25&until=2017-03-25&limit=100&offset=100&latest=true")
    
        #Artist TV Show Appearances
    def test_getArtistTVShowAppearances(self):
        self.assertEqual(caller.getArtistTVShowAppearances(3963),"https://api.chartmetric.com/api/artist/3963/tvmaze")

        #Artist Tiktok Audience Data
    def getArtistTiktokAudienceData(self):
        self.assertEqual(caller.getArtistTiktokAudienceData(3963),"https://api.chartmetric.com/api/artist/3963/tiktok-audience-stats")
        self.assertEqual(caller.getArtistTiktokAudienceData(3963, date="2020-09-20"),"https://api.chartmetric.com/api/artist/3963/tiktok-audience-stats?date=2020-09-20")

        #Artist Top Tracks by Platform
    def test_getArtistTopTracks(self):
        self.assertEqual(caller.getArtistTopTracks(3963, source="tiktok"),"https://api.chartmetric.com/api/artist/3963/top-tracks/tiktok")
        self.assertEqual(caller.getArtistTopTracks(3963, source="tiktok", limit=100),"https://api.chartmetric.com/api/artist/3963/top-tracks/tiktok?limit=100")

        #Artist Tracks
    def test_getArtistTracks(self):
        self.assertEqual(caller.getArtistTracks(3963),"https://api.chartmetric.com/api/artist/3963/tracks")
        self.assertEqual(caller.getArtistTracks(3963, offset=100),"https://api.chartmetric.com/api/artist/3963/tracks?offset=100")
        self.assertEqual(caller.getArtistTracks(3963, limit=100),"https://api.chartmetric.com/api/artist/3963/tracks?limit=100")
        self.assertEqual(caller.getArtistTracks(3963, offset=100, limit=100),"https://api.chartmetric.com/api/artist/3963/tracks?offset=100&limit=100")
        self.assertEqual(caller.getArtistTracks(3963, artistType="main"),"https://api.chartmetric.com/api/artist/3963/tracks?artist_type=main")
        self.assertEqual(caller.getArtistTracks(3963, offset=100, artistType="main"),"https://api.chartmetric.com/api/artist/3963/tracks?offset=100&artist_type=main")
        self.assertEqual(caller.getArtistTracks(3963, limit=100, artistType="main"),"https://api.chartmetric.com/api/artist/3963/tracks?limit=100&artist_type=main")
        self.assertEqual(caller.getArtistTracks(3963, offset=100, limit=100, artistType="main"),"https://api.chartmetric.com/api/artist/3963/tracks?offset=100&limit=100&artist_type=main")

        #Artist Youtube Audience Data
    def test_getArtistYoutubeAudience(self):
        self.assertEqual(caller.getArtistYoutubeAudience(3963),"https://api.chartmetric.com/api/artist/3963/youtube-audience-stats")
                       
        #Artist Youtube Views and Market Coverage
    def test_getArtistYoutubeViewsAndCoverage(self):
        self.assertEqual(caller.getArtistYoutubeViewsAndCoverage(3963),"https://api.chartmetric.com/api/artist/3963/market-coverage-views/youtube")

    #BRAND
        #Brand Info
    def test_getBrandInfo(self):
        self.assertEqual(caller.getBrandInfo(3963),"https://api.chartmetric.com/api/brand/3963")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers"),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers")
        self.assertEqual(caller.getBrandInfo(3963, sortOrderDesc=True),"https://api.chartmetric.com/api/brand/3963?sortOrderDesc=true")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", sortOrderDesc=True),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&sortOrderDesc=true")
        self.assertEqual(caller.getBrandInfo(3963, limit=100),"https://api.chartmetric.com/api/brand/3963?limit=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", limit=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&limit=100")
        self.assertEqual(caller.getBrandInfo(3963, sortOrderDesc=True, limit=100),"https://api.chartmetric.com/api/brand/3963?sortOrderDesc=true&limit=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", sortOrderDesc=True, limit=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&sortOrderDesc=true&limit=100")
        self.assertEqual(caller.getBrandInfo(3963, offset=100),"https://api.chartmetric.com/api/brand/3963?offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", offset=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortOrderDesc=True, offset=100),"https://api.chartmetric.com/api/brand/3963?sortOrderDesc=true&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", sortOrderDesc=True, offset=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&sortOrderDesc=true&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, limit=100, offset=100),"https://api.chartmetric.com/api/brand/3963?limit=100&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", limit=100, offset=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&limit=100&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortOrderDesc=True, limit=100, offset=100),"https://api.chartmetric.com/api/brand/3963?sortOrderDesc=true&limit=100&offset=100")
        self.assertEqual(caller.getBrandInfo(3963, sortColumn="followers", sortOrderDesc=True, limit=100, offset=100),"https://api.chartmetric.com/api/brand/3963?sortColumn=followers&sortOrderDesc=true&limit=100&offset=100")

        #Brand List by Interest
    def test_getBrandListbyInterest(self):
        self.assertEqual(caller.getBrandListbyInterest(),"https://api.chartmetric.com/api/brand/list/by/interest")
        self.assertEqual(caller.getBrandListbyInterest(sortColumn="followers"),"https://api.chartmetric.com/api/brand/list/by/interest?sortColumn=followers")

        #Brand List
    def test_getBrandList(self):
        self.assertEqual(caller.getBrandList(),"https://api.chartmetric.com/api/brand/list")

   #CHARTS

        #Charts Airplay
    def test_getChartsAirplay(self):
        self.assertEqual(caller.getChartsAirplay(chart_type="artists", date="2020-09-09", since="2020-09-09", limit=100, duration="daily"),"https://api.chartmetric.com/api/charts/airplay/artists?date=2020-09-09&since=2020-09-09&limit=100&duration=daily")
        self.assertEqual(caller.getChartsAirplay(chart_type="artists", date="2020-09-09", since="2020-09-09", limit=100, duration="daily", country_code="ES"),"https://api.chartmetric.com/api/charts/airplay/artists?date=2020-09-09&since=2020-09-09&limit=100&duration=daily&country_code=ES")
        self.assertEqual(caller.getChartsAirplay(chart_type="artists", date="2020-09-09", since="2020-09-09", limit=100, duration="daily", latest=True),"https://api.chartmetric.com/api/charts/airplay/artists?date=2020-09-09&since=2020-09-09&limit=100&duration=daily&latest=true")
        self.assertEqual(caller.getChartsAirplay(chart_type="artists", date="2020-09-09", since="2020-09-09", limit=100, duration="daily", country_code="ES", latest=True),"https://api.chartmetric.com/api/charts/airplay/artists?date=2020-09-09&since=2020-09-09&limit=100&duration=daily&country_code=ES&latest=true")
        
        #Charts Amazon
    def test_getChartsAmazon(self):
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres"),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", code2="ES"),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&code2=ES")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", offset=100),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&offset=100")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", code2="ES", offset=100),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&code2=ES&offset=100")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", latest=True),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&latest=true")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", code2="ES", latest=True),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&code2=ES&latest=true")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", offset=100, latest=True),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&offset=100&latest=true")
        self.assertEqual(caller.getChartsAmazon(chart_type="albums", sub_type="popular_track", date="2020-09-09", genre="All Genres", code2="ES", offset=100, latest=True),"https://api.chartmetric.com/api/charts/amazon/albums?type=popular_track&date=2020-09-09&genre=All+Genres&code2=ES&offset=100&latest=true")
 
        #Charts Apple Music
    def test_getChartsAppleMusic(self):
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES"),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", genre="All Genres"),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&genre=All+Genres")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, genre="All Genres"),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&genre=All+Genres")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", offset=100),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&offset=100")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, offset=100),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&offset=100")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", genre="All Genres", offset=100),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&genre=All+Genres&offset=100")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, genre="All Genres", offset=100),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&genre=All+Genres&offset=100")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", genre="All Genres", latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&genre=All+Genres&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, genre="All Genres", latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&genre=All+Genres&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", offset=100, latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&offset=100&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, offset=100, latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&offset=100&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", genre="All Genres", offset=100, latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&genre=All+Genres&offset=100&latest=true")
        self.assertEqual(caller.getChartsAppleMusic(chart_type="albums", sub_type="popular_track", date="2020-09-09", code2="ES", city_id=1, genre="All Genres", offset=100, latest=True),"https://api.chartmetric.com/api/charts/applemusic/albums?type=popular_track&date=2020-09-09&country_code=ES&city_id=1&genre=All+Genres&offset=100&latest=true")
        

        #Charts Beatport
    def test_getChartsBeatport(self):
        self.assertEqual(caller.getChartsBeatport(date="2019-02-01", genre="top-100"),"https://api.chartmetric.com/api/charts/beatport?date=2019-02-01&genre=top-100")
        self.assertEqual(caller.getChartsBeatport(date="2019-02-01", genre="top-100", offset=100),"https://api.chartmetric.com/api/charts/beatport?date=2019-02-01&genre=top-100&offset=100")
        self.assertEqual(caller.getChartsBeatport(date="2019-02-01", genre="top-100", latest=True),"https://api.chartmetric.com/api/charts/beatport?date=2019-02-01&genre=top-100&latest=true")
        self.assertEqual(caller.getChartsBeatport(date="2019-02-01", genre="top-100", offset=100, latest=True),"https://api.chartmetric.com/api/charts/beatport?date=2019-02-01&genre=top-100&offset=100&latest=true")

        #Charts Countries
    def test_getChartsCountries(self):
        self.assertEqual(caller.getChartsCountries(platform="tiktok", chart_type="tracks", sub_type="new_track", duration="daily"),"https://api.chartmetric.com/api/charts/tiktok/countries?chart_type=tracks&type=new_track&duration=daily")

 
        #Charts Chartmetric Score
    def test_getChartsChartmetricScore(self):
        self.assertEqual(caller.getChartsChartmetricScore(asset_type="track", type_id=1, chart_type="spotify-top", since="2017-03-25"),"https://api.chartmetric.com/api/charts/track/1/spotify-top/cm-score?since=2017-03-25")
        self.assertEqual(caller.getChartsChartmetricScore(asset_type="track", type_id=1, chart_type="spotify-top", since="2017-03-25", until="2017-03-25"),"https://api.chartmetric.com/api/charts/track/1/spotify-top/cm-score?since=2017-03-25&until=2017-03-25")

        #Charts Deezer
    def test_getChartsDeezer(self):
        self.assertEqual(caller.getChartsDeezer(country_code="US", date="2017-03-25"),"https://api.chartmetric.com/api/charts/deezer?country_code=US&date=2017-03-25")
        self.assertEqual(caller.getChartsDeezer(country_code="US", date="2017-03-25", latest=True),"https://api.chartmetric.com/api/charts/deezer?country_code=US&date=2017-03-25&latest=true")


        #Charts QQ Music
    def test_getChartsQQMusic(self):
        self.assertEqual(caller.getChartsQQMusic(date="2019-4-11"),"https://api.chartmetric.com/api/charts/qq?date=2019-4-11")
        self.assertEqual(caller.getChartsQQMusic(date="2019-4-11", latest=True),"https://api.chartmetric.com/api/charts/qq?date=2019-4-11&latest=true")
        
        #Charts Shazam (Cities)
    def test_getChartsQQMusic(self):
        self.assertEqual(caller.getChartsShazamCities(country_code="US"),"https://api.chartmetric.com/api/charts/shazam/US/cities")

        #Charts Shazam 
    def test_getChartsShazam(self):
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01"),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", city="San Francisco"),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&city=San%20Francisco")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", offest=100),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&offset=100")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", city="San Francisco"),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&city=San%20Francisco")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", offest=100, latest=True),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&offset=100&latest=true")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", city="San Francisco", latest=True),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&city=San%20Francisco&latest=true")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", offest=100, latest=True),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&offset=100&latest=true")
        self.assertEqual(caller.getChartsShazam(country_code="US",date="2020-09-01", city="San Francisco", latest=True),"https://api.chartmetric.com/api/charts/shazam?date=2020-09-01&country_code=US&city=San%20Francisco&latest=true")

        #Charts SoundCloud 
    def test_getChartsSoundCloud(self):
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music"),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", offest=100),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&offset=100")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", raw=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&raw=true")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", offest=100, raw=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&offset=100&raw=true")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", latest=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&latest=true")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", offest=100, latest=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&offset=100&latest=true")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", raw=True, latest=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&raw=true&latest=true")
        self.assertEqual(caller.getChartsSoundCloud(country_code="US",date="2020-09-01", kind="trending", genre="all-music", offest=100, raw=True, latest=True),"https://api.chartmetric.com/api/charts/soundcloud?date=2020-09-01&country_code=US&kind=trending&genre=all-music&offset=100&raw=true&latest=true")
  

        #Charts Spotify (Artists) 
    def test_getChartsSpotifyArtists(self):
        self.assertEqual(caller.getChartsSpotifyArtists(date="2020-09-01", chart_type="playlist_reach", interval="monthly"),"https://api.chartmetric.com/api/charts/spotify/artists?date=2020-09-01&interval=monthly&type=playlist_reach")
        self.assertEqual(caller.getChartsSpotifyArtists(date="2020-09-01", chart_type="playlist_reach", interval="monthly", offest=100),"https://api.chartmetric.com/api/charts/spotify/artists?date=2020-09-01&interval=monthly&type=playlist_reach&offset=100")
        self.assertEqual(caller.getChartsSpotifyArtists(date="2020-09-01", chart_type="playlist_reach", interval="monthly", latest=True),"https://api.chartmetric.com/api/charts/spotify/artists?date=2020-09-01&interval=monthly&type=playlist_reach&latest=true")
        self.assertEqual(caller.getChartsSpotifyArtists(date="2020-09-01", chart_type="playlist_reach", interval="monthly", offest=100, latest=True),"https://api.chartmetric.com/api/charts/spotify/artists?date=2020-09-01&interval=monthly&type=playlist_reach&offset=100&latest=true")

        #Charts Spotify (Freshfind) 
    def test_getChartsSpotifyFreshfind(self):
        self.assertEqual(caller.getChartsSpotifyFreshfind(date="2018-11-01"),"https://api.chartmetric.com/api/charts/spotify/freshfind?date=2018-11-01")
        self.assertEqual(caller.getChartsSpotifyFreshfind(date="2018-11-01", latest=True),"https://api.chartmetric.com/api/charts/spotify/freshfind?date=2018-11-01&latest=true")
        
        #Charts Spotify (Tracks) 
    def test_getChartsSpotifyTracks(self):
        self.assertEqual(caller.getChartsSpotifyTracks(date="2018-11-01", country_code="US", chart_type="regional", interval="daily"),"https://api.chartmetric.com/api/charts/spotify?date=2018-11-01&country_code=US&interval=daily&type=regional")
        self.assertEqual(caller.getChartsSpotifyTracks(date="2018-11-01", country_code="US", chart_type="regional", interval="daily", offset=100),"https://api.chartmetric.com/api/charts/spotify?date=2018-11-01&country_code=US&interval=daily&type=regional&offset=100")
        self.assertEqual(caller.getChartsSpotifyTracks(date="2018-11-01", country_code="US", chart_type="regional", interval="daily", latest=True),"https://api.chartmetric.com/api/charts/spotify?date=2018-11-01&country_code=US&interval=daily&type=regional&latest=true")
        self.assertEqual(caller.getChartsSpotifyTracks(date="2018-11-01", country_code="US", chart_type="regional", interval="daily", offset=100, latest=True),"https://api.chartmetric.com/api/charts/spotify?date=2018-11-01&country_code=US&interval=daily&type=regional&offset=100&latest=true")

        #Charts TikTok Top Tracks Stats (Freq Update)
    def test_getChartsTiktokTopTracksStats(self):
        self.assertEqual(caller.getChartsTiktokTopTracksStats(date="2018-11-01"),"https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date=2018-11-01")
        self.assertEqual(caller.getChartsTiktokTopTracksStats(date="2018-11-01", limit=100),"https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date=2018-11-01&limit=100")
        self.assertEqual(caller.getChartsTiktokTopTracksStats(date="2018-11-01", offset=100),"https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date=2018-11-01&offset=100")
        self.assertEqual(caller.getChartsTiktokTopTracksStats(date="2018-11-01", limit=100, offset=100),"https://api.chartmetric.com/api/charts/tiktok/top-tracks-stats?date=2018-11-01&limit=100&offset=100")

        #Charts TikTok
    def test_getChartsTiktok(self):
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes"),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", interval="all-time"),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11&interval=all-time")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", limit=100),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11&limit=100")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", offset=100),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11&offset=100")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", latest=True),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11&latest=true")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", countryChart=True, code2="US"),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11&countryChart=true&code2=US")
        self.assertEqual(caller.getChartsTiktok(chart_type="tracks", date="2020-10-11", user_chart_type="likes", code2="US"),"https://api.chartmetric.com/api/charts/tiktok/tracks?date=2020-10-11")


        #Charts Twitch
    def test_getChartsTwitch(self):
        self.assertEqual(caller.getChartsTwitch(since="2020-09-09", chart_type="followers", duration="daily", limit=100),"https://api.chartmetric.com/api/charts/twitch/users?since=2020-09-09&type=followers&duration=daily&limit=100")
        self.assertEqual(caller.getChartsTwitch(since="2020-09-09", chart_type="followers", duration="daily", limit=100, latest=True),"https://api.chartmetric.com/api/charts/twitch/users?since=2020-09-09&type=followers&duration=daily&limit=100&latest=true")


        #Charts Youtube
    def test_getChartsYoutube(self):
        self.assertEqual(caller.getChartsYoutube(chart_type="tracks", country_code="US", date="2020-02-06"),"https://api.chartmetric.com/api/charts/youtube/tracks?date=2020-02-06&country_code=US")
        self.assertEqual(caller.getChartsYoutube(chart_type="tracks", country_code="US", date="2020-02-06", offset=100),"https://api.chartmetric.com/api/charts/youtube/tracks?date=2020-02-06&country_code=US&offset=100")
        self.assertEqual(caller.getChartsYoutube(chart_type="tracks", country_code="US", date="2020-02-06", latest=True),"https://api.chartmetric.com/api/charts/youtube/tracks?date=2020-02-06&country_code=US&latest=true")
        self.assertEqual(caller.getChartsYoutube(chart_type="tracks", country_code="US", date="2020-02-06", offset=100, latest=True),"https://api.chartmetric.com/api/charts/youtube/tracks?date=2020-02-06&country_code=US&offset=100&latest=true")


        #Charts iTunes 
    def test_getChartsiTunes(self):
        self.assertEqual(caller.getChartsiTunes(chart_type="tracks", country_code="US", date="2018-11-01", genre="Pop"),"https://api.chartmetric.com/api/charts/itunes/tracks?date=2018-11-01&country_code=US&genre=Pop")
        self.assertEqual(caller.getChartsiTunes(chart_type="tracks", country_code="US", date="2018-11-01", genre="Pop", offset=100),"https://api.chartmetric.com/api/charts/itunes/tracks?date=2018-11-01&country_code=US&genre=Pop&offset=100")
        self.assertEqual(caller.getChartsiTunes(chart_type="tracks", country_code="US", date="2018-11-01", genre="Pop", latest=True),"https://api.chartmetric.com/api/charts/itunes/tracks?date=2018-11-01&country_code=US&genre=Pop&latest=true")
        self.assertEqual(caller.getChartsiTunes(chart_type="tracks", country_code="US", date="2018-11-01", genre="Pop", offset=100, latest=True),"https://api.chartmetric.com/api/charts/itunes/tracks?date=2018-11-01&country_code=US&genre=Pop&offset=100&latest=true")

    #CITY

        #Top Artists
    def test_getCityTopArtists(self):
        self.assertEqual(caller.getCityTopArtists(id=7060, source="spotify"),"https://api.chartmetric.com/api/city/7060/spotify/top-artists")
        #Top Tracks
    def test_getCityTopTracks(self):
        self.assertEqual(caller.getCityTopTracks(id=7060, source="spotify"),"https://api.chartmetric.com/api/city/7060/spotify/top-tracks")

    #CURATOR

        #Curator List
    def test_getCuratorList(self):
        self.assertEqual(caller.getCuratorList(platform="spotify"),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", offset=10, limit=None, editorial=None, majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", limit=10, editorial=None, majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", editorial=None, majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", majorLabel=None, brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", brand=None, popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", popularIndie=None, indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", indie=None, audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", audiobook=None, withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", withSocialUrls=None, code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", code2=None, aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")
        self.assertEqual(caller.getCuratorList(platform="spotify", aggregated=None),"https://api.chartmetric.com/api/curator/spotify/lists?indie=true&limit=5&offset=0&withSocialUrls=false")

        #Curator Fan Metrics
    def test_getCuratorFanMetrics(self):

        #Curator Metadata
    def test_getCuratorMetadata(self):

        #Curator Playlists
    def test_getCuratorPlaylists(self):

        #Curator Social / Streaming Service URLs
    def test_getCuratorSocialStreamingURLs(self):
        
'''                

    #PLAYLIST
    
        #Playlist Metadata
    def test_getPlaylistMetadata(self):

        #Playlist Evolution Stats (given Artist, Album or Track Chartmetric ID)
    def test_getPlaylistEvolutionStats(self):

        #Playlist Journey or Progression
    def test_getPlaylistJourneyProgression(self):

        #Playlist Last Updated Time
    def test_getPlaylistLastUpdatedTime(self):

        #Playlist List
    def test_getPlaylistList(self):
        
        #Playlist Snapshot
    def test_getPlaylistSnapshot(self):

        #Playlist Stats Over Time
    def test_getPlaylistStatsOverTime(self):

        #Playlist Tracks (Current, Past)
    def test_getPlaylistTracks(self):

    #RADIO
    
        #Radio Airplay information in Time Series
    def test_getRadioAirplayInfoinTime(self):

        #Radio Broadcast Market play counts
    def test_getRadioBroadcastPlayCounts(self):

        #Get Radio Station List for Country
    def test_getRadioStationList(self):

        #Radio Total Airplays
    def test_getRadioTotalAirplay(self):

    #RECOMMENDATION

        #Get 100 Similar Playlists
    def test_getRecommendationSimilarPlaylists(self):

    #SEARCH

        #Chartmetric Search Engine
    def test_search(self):

        #Get City Info
    def test_getCityInfo(self):

        #Get Genre Ids
    def test_getGenreIds(self):

    #TRACK 

        #Track Charts
    def test_getTrackCharts(self):
 
        #Track Get Track IDs
    def test_getTrackIDs(self):

        #Track Get Tracks (with filters)
    def test_getTracksWFilter(self):

        #Track Get Metadata
    def test_getTrackMetadata(self):

        #Track Playlist Snapshot
    def test_getTrackPlaylistSnapshot(self):

        #Track Playlist 
    def test_getTrackPlaylists(self):

        #Track Related Tracks 
    def test_getTrackRelatedTracks(self):

        #Track Stats 
    def test_getTrackStats(self):

        #Track Top TiVideo 
    def test_getTrackTopTiideo(self):
'''

if __name__ == '__main__':
    unittest.main()