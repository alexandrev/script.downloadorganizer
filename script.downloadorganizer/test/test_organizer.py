import unittest
import organizer

class TestOrganizer(unittest.TestCase):

  
  
  def test_upper(self):
      showRoot = 'Shows'
      movieRoot = 'Movie'
      self.assertEqual(organizer.generate_final_path('Lost.s01e01.Pilot Part 1 +C.mkv',showRoot,movieRoot), 'Shows/Lost/Season 1/Lost.s01e01.Pilot Part 1 +C.mkv')
      self.assertEqual(organizer.generate_final_path('under.the.dome.313.hdtv-lol.mp4',showRoot,movieRoot), 'Shows/Under The Dome/Season 3/under.the.dome.313.hdtv-lol.mp4')
      self.assertEqual(organizer.generate_final_path('Dominion.S02E10.HDTV.x264-KILLERS.mp4',showRoot,movieRoot), 'Shows/Dominion/Season 2/Dominion.S02E10.HDTV.x264-KILLERS.mp4')
      self.assertEqual(organizer.generate_final_path('Avengers.Age.of.Ultron.2015.1080p.BluRay.x264.YIFY.mp4',showRoot,movieRoot), 'Movie/Avengers.Age.of.Ultron.2015.1080p.BluRay.x264.YIFY/Avengers.Age.of.Ultron.2015.1080p.BluRay.x264.YIFY.mp4')
      self.assertEqual(organizer.generate_final_path('Fantastic.Four.2015.HC.HDRip.XViD.AC3-ETRG.avi',showRoot,movieRoot), 'Movie/Fantastic.Four.2015.HC.HDRip.XViD.AC3-ETRG/Fantastic.Four.2015.HC.HDRip.XViD.AC3-ETRG.avi')
      self.assertEqual(organizer.generate_final_path('Continuum.S04E02.HDTV.x264-KILLERS.mp4',showRoot,movieRoot), 'Shows/Continuum/Season 4/Continuum.S04E02.HDTV.x264-KILLERS.mp4')  
        

if __name__ == '__main__':
    unittest.main()
