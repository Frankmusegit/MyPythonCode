#!/usr/bin/env python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
# import from config.h
HAVE_FLOOR = 1
HAVE_INTTYPES_H = 1
HAVE_LIBSTDC__ = 1
HAVE_MEMORY_H = 1
HAVE_RINT = 1
HAVE_STDBOOL_H = 1
HAVE_STDINT_H = 1
HAVE_STDLIB_H = 1
HAVE_STRINGS_H = 1
HAVE_STRING_H = 1
HAVE_STRTOL = 1
HAVE_SYS_STAT_H = 1
HAVE_SYS_TYPES_H = 1
HAVE_UNISTD_H = 1
HAVE__BOOL = 1
NDEBUG = 1
STDC_HEADERS = 1
_NDEBUG = 1

#import from globals.h

debugMode = False
enableExperimental = False
scriptDebug = False
layoutDebug = False
enableInspector = False
noSeq = False
noMidi = False
midiInputTrace = False
midiOutputTrace = False
converterMode = False
noGui = False
converterDpi = 0.0

mimeSymbolFormat      = "application\mscore\symbol"
mimeSymbolListFormat  = "application\mscore\symbollist"
mimeStaffListFormat   = "application\mscore\stafflist"




class NoteHeadGroup:    
      HEAD_NORMAL = 0
      HEAD_CROSS =1
      HEAD_DIAMOND = 2
      HEAD_TRIANGLE =3
      HEAD_MI = 4
      HEAD_SLASH = 5
      HEAD_XCIRCLE = 6
      HEAD_DO = 7
      HEAD_RE = 8
      HEAD_FA = 9
      HEAD_LA = 10
      HEAD_TI = 11
      HEAD_SOL = 12
      HEAD_BREVIS_ALT = 13
      HEAD_GROUPS = 14

class NoteHeadType:
      HEAD_AUTO = 0
      HEAD_WHOLE = 1
      HEAD_HALF = 2
      HEAD_QUARTER = 3
      HEAD_BREVIS = 4

class Anchor:
      ANCHOR_SEGMENT = 0
      ANCHOR_MEASURE = 1

class Direction:
      AUTO = 0
      UP = 1
      DOWN = 2

class DirectionH:
      DH_AUTO = 0
      DH_LEFT = 1
      DH_RIGHT = 2

class ValueType:
      AUTO_VAL = 0
      USER_VAL = 1
      OFFSET_VAL = 2

class Placement:
      PLACE_AUTO = 0
      PLACE_ABOVE = 1
      PLACE_BELOW = 2
      PLACE_LEFT = 3

class LineSegmentType:
      SEGMENT_SINGLE = 0
      SEGMENT_BEGIN = 1
      SEGMENT_MIDDLE = 2
      SEGMENT_END = 3

class AlignmentFlags:
      ALIGN_LEFT     = 0
      ALIGN_RIGHT    = 1
      ALIGN_HCENTER  = 2
      ALIGN_TOP      = 0
      ALIGN_BOTTOM   = 4
      ALIGN_VCENTER  = 8
      ALIGN_BASELINE = 16
      ALIGN_CENTER = ALIGN_HCENTER | ALIGN_VCENTER
      

class OffsetType:
      OFFSET_ABS = 0
      OFFSET_SPATIUM = 1

class BeamMode:
      BEAM_AUTO = 0
      BEAM_BEGIN = 1
      BEAM_MID = 2
      BEAM_END = 3
      BEAM_NO = 4
      BEAM_BEGIN32 = 5
      BEAM_INVALID = 6

class TransposeDirection:
      TRANSPOSE_UP = 0
      TRANSPOSE_DOWN = 1
      TRANSPOSE_CLOSEST = 2
      
class TransposeMode:
      TRANSPOSE_BY_KEY = 0
      TRANSPOSE_BY_INTERVAL = 1

class NoteType:
      NOTE_NORMAL = 0
      NOTE_ACCIACCATURA = 1
      NOTE_APPOGGIATURA = 2
      NOTE_GRACE4 = 3
      NOTE_GRACE16 = 4
      NOTE_GRACE32 = 5
      NOTE_INVALID = 6

class SelectType:
      SELECT_SINGLE = 0
      SELECT_RANGE = 1
      SELECT_ADD = 2

class SS:
      STATE_INIT = 0
      STATE_DISABLED = 1
      STATE_NORMAL = 2
      STATE_NOTE_ENTRY = 4
      STATE_EDIT = 8
      STATE_PLAY = 16
      STATE_SEARCH = 32

class SelState:
      SEL_NONE = 0
      SEL_LIST = 1
      SEL_RANGE = 2

class SeqState:
    STOP = 0
    PLAY = 1
    START_PLAY = 2

class MAG:
       MAG_25 = 0
       MAG_50 = 1
       MAG_75 = 2
       MAG_100 = 3
       MAG_150 = 4
       MAG_200 = 5
       MAG_400 = 6
       MAG_800 = 7
       MAG_1600 = 8
       MAG_PAGE_WIDTH = 9
       MAG_PAGE = 10
       MAG_DBL_PAGE = 11
       MAG_FREE = 12

class IconNames1:
      ICON_ACCIACCATURA = 0
      ICON_APPOGGIATURA = 1
      ICON_GRACE4 = 2
      ICON_GRACE16 = 3
      ICON_GRACE32 = 4
      ICON_SBEAM = 5
      ICON_MBEAM = 6
      ICON_NBEAM = 7
      ICON_BEAM32 = 8
      ICON_AUTOBEAM = 9
      
class IconNames2:
      longaUp_ICON = 0
      brevis_ICON = 1
      note_ICON = 2
      note2_ICON = 3
      note4_ICON = 4
      note8_ICON = 5
      note16_ICON = 6
      note32_ICON = 7
      note64_ICON = 8
      natural_ICON = 9
      sharp_ICON = 10
      sharpsharp_ICON = 11
      flat_ICON = 12
      flatflat_ICON = 13
      staccato_ICON = 14
      quartrest_ICON = 15
      dot_ICON = 16
      dotdot_ICON = 17
      sforzatoaccent_ICON = 18
      tenuto_ICON = 19
      plus_ICON = 20
      flip_ICON = 21
      voice1_ICON = 22
      voice2_ICON = 23
      voice3_ICON = 24
      voice4_ICON = 25
      undo_ICON = 26
      redo_ICON = 27
      cut_ICON = 28
      copy_ICON = 29
      paste_ICON = 30
      print_ICON = 31
      clef_ICON = 32
      midiin_ICON = 33
      speaker_ICON = 34
      start_ICON = 35
      play_ICON = 36
      repeat_ICON = 37
      sbeam_ICON = 38
      mbeam_ICON = 39
      nbeam_ICON = 40
      beam32_ICON = 41
      abeam_ICON = 42
      fileOpen_ICON = 43
      fileNew_ICON = 44
      fileSave_ICON = 45
      fileSaveAs_ICON = 46
      exit_ICON = 47
      viewmag_ICON = 48
      window_ICON = 49
      acciaccatura_ICON = 50
      appoggiatura_ICON = 51
      grace4_ICON = 52
      grace16_ICON = 53
      grace32_ICON = 54
      noteEntry_ICON = 55
      keys_ICON = 56
      tie_ICON = 57
      community_ICON = 58
      ICONS = 59

class TEXT_STYLE:
      TEXT_STYLE_SYMBOL1 = 0
      TEXT_STYLE_SYMBOL3 = 1
      TEXT_STYLE_TITLE = 2
      TEXT_STYLE_SUBTITLE = 3
      TEXT_STYLE_COMPOSER = 4
      TEXT_STYLE_POET = 5
      TEXT_STYLE_LYRIC1 = 6
      TEXT_STYLE_LYRIC2 = 7
      TEXT_STYLE_FINGERING = 8
      TEXT_STYLE_INSTRUMENT_LONG = 9
      TEXT_STYLE_INSTRUMENT_SHORT = 10
      TEXT_STYLE_INSTRUMENT_EXCERPT = 11
      TEXT_STYLE_DYNAMICS = 12
      TEXT_STYLE_TECHNIK = 13
      TEXT_STYLE_TEMPO = 14
      TEXT_STYLE_METRONOME = 15
      TEXT_STYLE_COPYRIGHT = 16
      TEXT_STYLE_MEASURE_NUMBER = 17
      TEXT_STYLE_PAGE_NUMBER_ODD = 18
      TEXT_STYLE_PAGE_NUMBER_EVEN = 19
      TEXT_STYLE_TRANSLATOR = 20

      TEXT_STYLE_TUPLET = 21
      TEXT_STYLE_SYSTEM = 22
      TEXT_STYLE_STAFF = 23
      TEXT_STYLE_HARMONY = 24
      TEXT_STYLE_REHEARSAL_MARK = 25
      TEXT_STYLE_REPEAT = 26
      TEXT_STYLE_VOLTA = 27
      TEXT_STYLE_FRAME = 28
      TEXT_STYLE_TEXTLINE = 29
      TEXT_STYLE_GLISSANDO = 30
      TEXT_STYLE_STRING_NUMBER = 31
      TEXT_STYLE_OTTAVA = 32
      TEXT_STYLES = 33

class StyleValueType:
      ST_SPATIUM = 0
      ST_DOUBLE = 1
      ST_BOOL = 2
      ST_INT = 3
      ST_DIRECTION = 4
      ST_STRING = 5

class StyleIdx:
      ST_staffUpperBorder = 0
      ST_staffLowerBorder = 1
      ST_staffDistance= 2
      ST_akkoladeDistance= 3
      ST_systemDistance = 4
      ST_lyricsDistance = 5
      ST_lyricsMinBottomDistance = 6
      ST_systemFrameDistance = 7
      ST_frameSystemDistance = 8
      ST_minMeasureWidth = 9

      ST_barWidth = 10
      ST_doubleBarWidth = 11
      ST_endBarWidth = 12
      ST_doubleBarDistance = 13
      ST_endBarDistance = 14
      ST_repeatBarTips = 15
      ST_startBarlineSingle = 16
      ST_startBarlineMultiple = 17

      ST_bracketWidth = 18
      ST_bracketDistance = 19
      ST_clefLeftMargin = 20
      ST_keysigLeftMargin = 21
      ST_timesigLeftMargin =22

      ST_clefKeyRightMargin = 23
      ST_clefBarlineDistance = 24
      ST_stemWidth = 25
      ST_shortenStem = 26
      ST_shortStemProgression = 27
      ST_shortestStem = 28
      ST_beginRepeatLeftMargin = 29
      ST_minNoteDistance = 30
      ST_barNoteDistance = 31
      ST_noteBarDistance = 32 

      ST_measureSpacing  = 33
      ST_staffLineWidth= 34
      ST_ledgerLineWidth = 35
      ST_akkoladeWidth = 36
      ST_accidentalDistance = 37
      ST_accidentalNoteDistance = 38
      ST_beamWidth = 39
      ST_beamDistance= 40
      ST_beamMinLen = 41
      ST_beamMinSlope = 42

      ST_beamMaxSlope = 43
      ST_maxBeamTicks = 44
      ST_dotNoteDistance = 45
      ST_dotRestDistance = 46
      ST_dotDotDistance = 47
      ST_propertyDistanceHead = 48
      ST_propertyDistanceStem = 49
      ST_propertyDistance = 50
      ST_pageFillLimit = 51
      ST_lastSystemFillLimit = 52

      ST_hairpinHeight = 53
      ST_hairpinContHeight = 54
      ST_hairpinWidth = 55
      ST_showPageNumber = 56
      ST_showPageNumberOne = 57
      ST_pageNumberOddEven = 58
      ST_showMeasureNumber = 59
      ST_showMeasureNumberOne = 60
      ST_measureNumberInterval = 61
      ST_measureNumberSystem = 62

      ST_measureNumberAllStaffs = 63
      ST_smallNoteMag = 64
      ST_graceNoteMag = 65
      ST_smallStaffMag = 66
      ST_smallClefMag = 67
      ST_genClef = 68
      ST_genKeysig = 69
      ST_genTimesig = 70
      ST_genCourtesyTimesig = 71
      ST_genCourtesyKeysig = 72


      ST_useGermanNoteNames = 73
      ST_chordDescriptionFile = 74
      ST_concertPitch = 75
      ST_createMultiMeasureRests = 76
      ST_minEmptyMeasures = 77
      ST_minMMRestWidth = 78
      ST_hideEmptyStaves= 79
      ST_stemDir1 = 80
      ST_stemDir2 = 81

      ST_stemDir3 = 82
      ST_stemDir4 = 83
      ST_gateTime = 84
      ST_tenutoGateTime = 85
      ST_staccatoGateTime = 86
      ST_slurGateTime = 87

      ST_UfermataAnchor = 88
      ST_DfermataAnchor = 89
      ST_UshortfermataAnchor = 90
      ST_DshortfermataAnchor = 91
      ST_UlongfermataAnchor = 92
      ST_DlongfermataAnchor = 93
      ST_UverylongfermataAnchor = 94
      ST_DverylongfermataAnchor = 95
      ST_ThumbAnchor = 96
      ST_SforzatoaccentAnchor = 97
      ST_EspressivoAnchor = 98
      ST_StaccatoAnchor = 99

      ST_UstaccatissimoAnchor = 100
      ST_DstaccatissimoAnchor = 101
      ST_TenutoAnchor = 102
      ST_UportatoAnchor = 103
      ST_DportatoAnchor = 104
      ST_UmarcatoAnchor = 105
      ST_DmarcatoAnchor = 106
      ST_OuvertAnchor = 107
      ST_PlusstopAnchor = 108
      ST_UpbowAnchor = 109

      ST_DownbowAnchor = 110
      ST_ReverseturnAnchor = 111
      ST_TurnAnchor = 112
      ST_TrillAnchor = 113
      ST_PrallAnchor = 114
      ST_MordentAnchor = 115
      ST_PrallPrallAnchor = 116
      ST_PrallMordentAnchor = 117
      ST_UpPrallAnchor = 118
      ST_DownPrallAnchor = 119

      ST_UpMordentAnchor = 120
      ST_DownMordentAnchor = 121
      ST_SnappizzicatoAnchor = 122
      ST_ArpeggioNoteDistance = 123
      ST_ArpeggioLineWidth = 124
      ST_ArpeggioHookLen = 125
      ST_FixMeasureNumbers = 126
      ST_FixMeasureWidth = 127

      ST_STYLES = 128

class ArticulationAnchor:
      A_TOP_STAFF = 0
      A_BOTTOM_STAFF = 1
      A_CHORD = 2       
      A_TOP_CHORD = 3     
      A_BOTTOM_CHORD = 4  


class SV:
      NORMAL = 0
      DRAG = 1
      DRAG_OBJECT = 2
      EDIT = 3
      DRAG_EDIT = 4
      LASSO = 5
      NOTE_ENTRY = 6
      MAG = 7
      PLAY = 8
      SEARCH = 9
      ENTRY_PLAY = 10
      STATES = 11
      
ICON_HEIGHT = 30
ICON_WIDTH  = 24




##import from Preference.h
class SessionStart:
      EMPTY_SESSION = 0
      LAST_SESSION = 1
      NEW_SESSION = 2
      SCORE_SESSION = 3
      
class MidiRemote:
      channel = 0
      Type = 0
      data = 0
      

midiActionMap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class TEXT:
      TEXT_UNKNOWN = 0
      TEXT_TITLE =1
      TEXT_SUBTITLE = 2
      TEXT_COMPOSER = 3
      TEXT_POET = 4
      TEXT_TRANSLATOR = 5
      TEXT_MEASURE_NUMBER = 6
      TEXT_PAGE_NUMBER_ODD = 7
      TEXT_PAGE_NUMBER_EVEN = 7
      TEXT_COPYRIGHT = 8
      TEXT_FINGERING = 9
      TEXT_INSTRUMENT_LONG = 10
      TEXT_INSTRUMENT_SHORT = 11
      TEXT_INSTRUMENT_EXCERPT = 12
      TEXT_TEMPO = 13
      TEXT_LYRIC = 14
      TEXT_TUPLET = 15
      TEXT_SYSTEM  = 16
      TEXT_STAFF = 17
      TEXT_CHORD = 18
      TEXT_REHEARSAL_MARK = 19
      TEXT_REPEAT = 20
      TEXT_VOLTA = 21
      TEXT_FRAME = 22
      TEXT_TEXTLINE  = 23
      TEXT_STRING_NUMBER = 24
      
class TSIG:
      TSIG_FOUR_FOUR  = 0x40000104
      TSIG_ALLA_BREVE = 0x40002084


class SEQ:
       STOP = 0
       PLAY = 1
       START_PLAY = 2

class MAG:
       MAG_25 = 0
       MAG_50 = 1
       MAG_75 = 2
       MAG_100 = 3
       MAG_150 = 4
       MAG_200 = 5
       MAG_400 = 6
       MAG_800 = 7
       MAG_1600 = 8
       MAG_PAGE_WIDTH = 9
       MAG_PAGE = 10
       MAG_DBL_PAGE = 11
       MAG_FREE = 12

class ElementType:
      INVALID = -1
      SYMBOL  = 0
      TEXT = 1
      SLUR_SEGMENT = 2
      BAR_LINE = 3
      STEM_SLASH = 4
      LINE = 5
      BRACKET = 6
      ARPEGGIO = 7
      ACCIDENTAL = 8
      NOTE = 9
      STEM = 10
      CLEF = 11
      KEYSIG = 12
      TIMESIG = 13
      REST = 14
      BREATH = 15
      GLISSANDO = 16
      REPEAT_MEASURE = 17
      IMAGE = 18
      ARTICULATION = 19
      DYNAMIC = 20
      PAGE = 21
      BEAM = 22
      HOOK = 23
      LYRICS = 24
      MARKER = 25
      JUMP = 26
      TUPLET = 27
      TEMPO_TEXT = 28
      STAFF_TEXT = 29
      HARMONY = 30
      VOLTA = 31
      HAIRPIN_SEGMENT = 32
      OTTAVA_SEGMENT = 33
      PEDAL_SEGMENT = 34
      TRILL_SEGMENT = 35
      TEXTLINE_SEGMENT = 36
      VOLTA_SEGMENT = 37
      LAYOUT_BREAK = 38
      SPACER = 39
      LEDGER_LINE = 40
      NOTEHEAD = 41
      TREMOLO = 42
      MEASURE = 43
      STAFF_LINES = 44
      CURSOR = 45
      SELECTION = 46
      LASSO = 47
      SHADOW_NOTE = 48
      RUBBERBAND = 49

      HAIRPIN = 50
      OTTAVA = 51
      PEDAL = 52
      TRILL = 53
      TEXTLINE = 54
      SEGMENT = 55
      SYSTEM = 56
      COMPOUND = 57
      CHORD = 58
      SLUR = 59

      ELEMENT = 60
      ELEMENT_LIST = 61
      STAFF_LIST = 62
      MEASURE_LIST = 63
      LAYOUT = 64
      HBOX = 65
      VBOX = 66
      ICON = 67
      ACCIDENTAL_BRACKET = 68
      MAXTYPE = 69

class DynamicType:
    DYNAMIC_STAFF = 0
    DYNAMIC_PART = 1
    DYNAMIC_SYSTEM = 2

class Type:
    Horizontal = 0
    Vertical = 1
    Leaf = 2

class SegmentType:
      SegClef                 = 0x1
      SegKeySig               = 0x2
      SegTimeSig              = 0x4
      SegStartRepeatBarLine   = 0x8
      SegBarLine              = 0x10
      SegGrace                = 0x20
      SegChordRest            = 0x40
      SegBreath               = 0x80
      SegEndBarLine           = 0x100
      SegTimeSigAnnounce      = 0x200
      SegKeySigAnnounce       = 0x400
      SegAll                  = 0xfff

class DurationType:
    V_LONG = 0
    V_BREVE = 1
    V_WHOLE = 2
    V_HALF = 3
    V_QUARTER = 4
    V_EIGHT = 5
    V_16TH = 6
    V_32ND = 7
    V_64TH = 8
    V_128TH = 9
    V_256TH = 10
    V_ZERO = 11
    V_MEASURE = 12
    V_INVALID = 13

class BarType:
    NORMAL_BAR = 0
    DOUBLE_BAR = 1
    START_REPEAT = 2
    END_REPEAT = 3
    BROKEN_BAR = 4
    END_BAR = 5
    END_START_REPEAT = 6

class VOLTA:
    VOLTA_OPEN = 0
    VOLTA_CLOSED = 1

class LAYOUT:
    LAYOUT_BREAK_PAGE = 0
    LAYOUT_BREAK_LINE = 1

class BRACKET:
    BRACKET_NORMAL = 0
    BRACKET_AKKOLADE = 1
    NO_BRACKET = -1

class ArticulationIdx:
      UfermataSym = 0
      DfermataSym = 1
      UshortfermataSym = 2
      DshortfermataSym = 3
      UlongfermataSym = 4
      DlongfermataSym = 5
      UverylongfermataSym = 6
      DverylongfermataSym = 7
      ThumbSym = 8
      SforzatoaccentSym = 9
      EspressivoSym = 10
      StaccatoSym = 11
      UstaccatissimoSym = 12
      DstaccatissimoSym = 13
      TenutoSym = 14
      UportatoSym = 15
      DportatoSym = 16
      UmarcatoSym = 17
      DmarcatoSym = 18
      OuvertSym = 19
      PlusstopSym = 20
      UpbowSym = 21
      DownbowSym = 22
      ReverseturnSym = 23
      TurnSym = 24
      TrillSym = 25
      PrallSym = 26
      MordentSym = 27
      PrallPrallSym = 28
      PrallMordentSym = 29
      UpPrallSym = 30
      DownPrallSym = 31
      UpMordentSym = 32
      DownMordentSym = 33
      SnappizzicatoSym = 34
      ARTICULATIONS = 35

class AccidentalType:
      ACC_NONE = 0
      ACC_SHARP = 1
      ACC_FLAT = 2
      ACC_SHARP2 = 3
      ACC_FLAT2 = 4
      ACC_NATURAL = 5

      ACC_FLAT_SLASH = 6
      ACC_FLAT_SLASH2 = 7
      ACC_MIRRORED_FLAT2 = 8
      ACC_MIRRORED_FLAT = 9
      ACC_MIRRIRED_FLAT_SLASH = 10
      ACC_FLAT_FLAT_SLASH = 11

      ACC_SHARP_SLASH = 12
      ACC_SHARP_SLASH2 = 13
      ACC_SHARP_SLASH3 = 14
      ACC_SHARP_SLASH4 = 15

      ACC_SHARP_ARROW_UP = 16
      ACC_SHARP_ARROW_DOWN = 17
      ACC_SHARP_ARROW_BOTH = 18
      ACC_FLAT_ARROW_UP = 19
      ACC_FLAT_ARROW_DOWN = 20
      ACC_FLAT_ARROW_BOTH = 21
      ACC_NATURAL_ARROW_UP = 22
      ACC_NATURAL_ARROW_DOWN = 23
      ACC_NATURAL_ARROW_BOTH = 24
      ACC_SORI = 25
      ACC_KORON = 26
      ACC_END = 27

class DynamicType:
    DYNAMIC_STAFF = 0
    DYNAMIC_PART = 1
    DYNAMIC_SYSTEM = 2

class CLEF:
      CLEF_G = 0
      CLEF_G1 = 1
      CLEF_G2 = 2
      CLEF_G3 = 3
      CLEF_F = 4
      CLEF_F8 = 5
      CLEF_F15 = 6
      CLEF_F_B = 7
      CLEF_F_C = 8
      CLEF_C1 = 9
      CLEF_C2 = 10
      CLEF_C3 = 11
      CLEF_C4 = 12
      CLEF_TAB = 13
      CLEF_PERC = 14
      CLEF_C5 = 15
      CLEF_G4 = 16
      CLEF_F_8VA = 17
      CLEF_F_15MA = 18
      CLEF_PERC2 = 19
      CLEF_MAX = 20

class SelState:
      SEL_NONE = 0
      SEL_LIST = 1
      SEL_RANGE = 2

class CLEF:
      CLEF_G = 0
      CLEF_G1 = 1
      CLEF_G2 = 2
      CLEF_G3 = 3
      CLEF_F = 4
      CLEF_F8 = 5
      CLEF_F15 = 6
      CLEF_F_B = 7
      CLEF_F_C = 8
      CLEF_C1 = 9
      CLEF_C2 = 10
      CLEF_C3 = 11
      CLEF_C4 = 12
      CLEF_TAB = 13
      CLEF_PERC = 14
      CLEF_C5 = 15
      CLEF_G4 = 16
      CLEF_F_8VA = 17
      CLEF_F_15MA = 18
      CLEF_PERC2 = 19
      CLEF_MAX = 20

class MARKER:
      MARKER_SEGNO = 0
      MARKER_CODA = 1
      MARKER_VARCODA = 2
      MARKER_CODETTA = 3
      MARKER_FINE = 4
      MARKER_TOCODA = 5
      MARKER_USER = 6

class JUMP:
      JUMP_DC = 0
      JUMP_DC_AL_FINE = 1
      JUMP_DC_AL_CODA = 2
      JUMP_DS_AL_CODA = 3
      JUMP_DS_AL_FINE = 4
      JUMP_DS = 5
      JUMP_USER = 6

class PaletteCommand:
      PALETTE_DELETE = 0
      PALETTE_EDIT = 1
      PALETTE_UP = 2
      PALETTE_DOWN = 3
      PALETTE_NEW = 4

class ME:
      ME_NOTEOFF    = 0x80
      ME_NOTEON     = 0x90
      ME_POLYAFTER  = 0xa0
      ME_CONTROLLER = 0xb0
      ME_PROGRAM    = 0xc0
      ME_AFTERTOUCH = 0xd0
      ME_PITCHBEND  = 0xe0
      ME_SYSEX      = 0xf0
      ME_META       = 0xff
      ME_SONGPOS    = 0xf2
      ME_ENDSYSEX   = 0xf7
      ME_CLOCK      = 0xf8
      ME_START      = 0xfa
      ME_CONTINUE   = 0xfb
      ME_STOP       = 0xfc
      ME_NOTE       = 0x100
      ME_CHORD      = 0x101
      
class META:
      META_SEQUENCE_NUMBER = 0
      META_TEXT            = 1
      META_COPYRIGHT       = 2
      META_TRACK_NAME      = 3
      META_INSTRUMENT_NAME = 4
      META_LYRIC           = 5
      META_MARKER          = 6
      META_CUE_POINT       = 7
      META_TITLE           = 8
      META_SUBTITLE        = 9
      META_COMPOSER        = 0xa
      META_TRANSLATOR      = 0xb
      META_POET            = 0xc   
      META_TRACK_COMMENT   = 0xf
      META_PORT_CHANGE     = 0x21
      META_CHANNEL_PREFIX  = 0x22
      META_TEMPO           = 0x51
      META_TIME_SIGNATURE  = 0x58
      META_KEY_SIGNATURE   = 0x59

class CTRL:
      CTRL_HBANK              = 0x00
      CTRL_LBANK              = 0x20
      CTRL_HDATA              = 0x06
      CTRL_LDATA              = 0x26
      CTRL_HNRPN              = 0x63
      CTRL_LNRPN              = 0x62
      CTRL_HRPN               = 0x65
      CTRL_LRPN               = 0x64
      CTRL_MODULATION         = 0x01
      CTRL_PORTAMENTO_TIME    = 0x05
      CTRL_VOLUME             = 0x07
      CTRL_PANPOT             = 0x0a
      CTRL_EXPRESSION         = 0x0b
      CTRL_SUSTAIN            = 0x40
      CTRL_PORTAMENTO         = 0x41
      CTRL_SOSTENUTO          = 0x42
      CTRL_SOFT_PEDAL         = 0x43
      CTRL_HARMONIC_CONTENT   = 0x47
      CTRL_RELEASE_TIME       = 0x48
      CTRL_ATTACK_TIME        = 0x49

      CTRL_BRIGHTNESS         = 0x4a
      CTRL_PORTAMENTO_CONTROL = 0x54
      CTRL_REVERB_SEND        = 0x5b
      CTRL_CHORUS_SEND        = 0x5d
      CTRL_VARIATION_SEND     = 0x5e

      CTRL_ALL_SOUNDS_OFF     = 0x78
      CTRL_RESET_ALL_CTRL     = 0x79
      CTRL_LOCAL_OFF          = 0x7a

      CTRL_PROGRAM   = 0x40001
      CTRL_PITCH     = 0x40002
      CTRL_PRESS     = 0x40003
      CTRL_POLYAFTER = 0x40004

INCH = 25.4
PPI  = 72.0           #printer points per inch
SPATIUM20 = 5.0 / PPI #size of Spatium for 20pt font in inch
VOICES = 4
MAX_STAVES = 4
DPMM_DISPLAY = 4   # 100 DPI
PALETTE_SPATIUM = 1.9 * DPMM_DISPLAY

MAX_LYRICS       = 8
MAX_PART_GROUPS  = 8
MAX_NUMBER_LEVEL = 6
MAX_BRACKETS     = 8
MAX_DASHES       = 8

guiRefresh   = 20
peakHoldTime = 1400
peakHold     = (peakHoldTime * guiRefresh) / 1000

debugMode       = False
layoutDebug     =  False
scriptDebug     =  False
noSeq           =  False
noMidi          =  False
midiInputTrace  =  False
midiOutputTrace =  False
showRubberBand  =  True
useFactorySettings = False
RECENT_LIST_SIZE = 10
VERSION = 1.0
useALSA = False
useJACK = False
usePortaudio = False