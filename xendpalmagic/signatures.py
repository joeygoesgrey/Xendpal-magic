mime_types = {
  "3gp": "video/3gpp",
  "3gpp": "video/3gpp",
  "7z": "application/x-7z-compressed",
  "ai": "application/postscript",
  "asf": "video/x-ms-asf",
  "asx": "video/x-ms-asf",
  "atom": "application/atom+xml",
  "avi": "video/x-msvideo",
  "bin": "application/octet-stream",
  "bmp": "image/x-ms-bmp",
  "cco": "application/x-cocoa",
  "crt": "application/x-x509-ca-cert",
  "css": "text/css",
  "deb": "application/octet-stream",
  "der": "application/x-x509-ca-cert",
  "dll": "application/octet-stream",
  "dmg": "application/octet-stream",
  "doc": "application/msword",
  "ear": "application/java-archive",
  "eot": "application/octet-stream",
  "eps": "application/postscript",
  "exe": "application/octet-stream",
  "flv": "video/x-flv",
  "gif": "image/gif",
  "hqx": "application/mac-binhex40",
  "htc": "text/x-component",
  "htm": "text/html",
  "html": "text/html",
  "ico": "image/x-icon",
  "img": "application/octet-stream",
  "iso": "application/octet-stream",
  "jad": "text/vnd.sun.j2me.app-descriptor",
  "jar": "application/java-archive",
  "jardiff": "application/x-java-archive-diff",
  "jng": "image/x-jng",
  "jnlp": "application/x-java-jnlp-file",
  "jpeg": "image/jpeg",
  "jpg": "image/jpeg",
  "js": "application/x-javascript",
  "json": "application/json",
  "kar": "audio/midi",
  "kml": "application/vnd.google-earth.kml+xml",
  "kmz": "application/vnd.google-earth.kmz",
  "m4a": "audio/x-m4a",
  "m4v": "video/x-m4v",
  "mid": "audio/midi",
  "midi": "audio/midi",
  "mml": "text/mathml",
  "mng": "video/x-mng",
  "mov": "video/quicktime",
  "mp3": "audio/mpeg",
  "mp4": "video/mp4",
  "mpeg": "video/mpeg",
  "mpg": "video/mpeg",
  "msi": "application/octet-stream",
  "msm": "application/octet-stream",
  "msp": "application/octet-stream",
  "ogg": "audio/ogg",
  "pdb": "application/x-pilot",
  "pdf": "application/pdf",
  "pem": "application/x-x509-ca-cert",
  "pl": "application/x-perl",
  "pm": "application/x-perl",
  "png": "image/png",
  "ppt": "application/vnd.ms-powerpoint",
  "prc": "application/x-pilot",
  "ps": "application/postscript",
  "ra": "audio/x-realaudio",
  "rar": "application/x-rar-compressed",
  "rpm": "application/x-redhat-package-manager",
  "rss": "application/rss+xml",
  "rtf": "application/rtf",
  "run": "application/x-makeself",
  "sea": "application/x-sea",
  "shtml": "text/html",
  "sit": "application/x-stuffit",
  "svg": "image/svg+xml",
  "svgz": "image/svg+xml",
  "swf": "application/x-shockwave-flash",
  "tcl": "application/x-tcl",
  "tif": "image/tiff",
  "tiff": "image/tiff",
  "tk": "application/x-tcl",
  "txt": "text/plain",
  "war": "application/java-archive",
  "wbmp": "image/vnd.wap.wbmp",
  "webm": "video/webm",
  "webp": "image/webp",
  "wml": "text/vnd.wap.wml",
  "wmlc": "application/vnd.wap.wmlc",
  "wmv": "video/x-ms-wmv",
  "xhtml": "application/xhtml+xml",
  "xls": "application/vnd.ms-excel",
  "xml": "text/xml",
  "xpi": "application/x-xpinstall",
  "zip": "application/zip"
}

file_signatures = {
  "webm": {
    "hex_signature": ["1A 45 DF A3"],
    "description": "WebM video file",
    "mime_type": mime_types.get("webm")
  },
  "flv": {
    "hex_signature": ["46 4C 56"],
    "description": "Flash video file",
    "mime_type": mime_types.get("flv")
  },
  "asf": {
    "hex_signature": ["30 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C"],
    "description": "Advanced Systems Format (ASF) file",
    "mime_type": mime_types.get("asf")
  },
  "wmv": {
    "hex_signature": ["30 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C"],
    "description": "Windows Media Video file",
    "mime_type": mime_types.get("wmv")
  },
  "avi": {
    "hex_signature": ["52 49 46 46", "41 56 49 20"],
    "description": "Audio Video Interleave (AVI) file",
    "mime_type": mime_types.get("avi")
  },
  "3gp":{
    "hex_signature": [
      "66 74 79 70 33 67",
    ],
    "description": "3rd Generation Partnership Project 3GPP and 3GPP2 multimedia files",
    "mime_type": mime_types.get("3gp")
  },
  "mp4":{
    "hex_signature": [
      "66 74 79 70 4D 53 4E 56",
      "66 74 79 70 69 73 6F 6D",
    ],
    "description": "MPEG-4 audio or video container",
    "mime_type": mime_types.get("mp4")
  },
  "mpeg":{
     "hex_signature": [
      "47"
    ],
    "description": "MPEG-1 video stream",
    "mime_type": mime_types.get("mpeg") 
  },
  "mpg":{
    "hex_signature": [
      "47"
    ],
    "description": "MPEG-1 video stream",
    "mime_type": mime_types.get("mpg")
  },
  
  "html": {
    "hex_signature": [
      "63 74 79 70 65 20"  # Likely starts with HTML doctype declaration
    ],
    "description": "HTML document",
    "mime_type": mime_types.get("html")
  },
  "htm": {
    "hex_signature": [
      "63 74 79 70 65 20"  # Likely starts with HTML doctype declaration
    ],
    "description": "HTML document",
    "mime_type": mime_types.get("htm")
  },
  "shtml": {
    "hex_signature": [
      "63 74 79 70 65 20"  # Likely starts with HTML doctype declaration
    ],
    "description": "Server-side scripting HTML document",
    "mime_type": mime_types.get("shtml")
  },
  "css": {
    "hex_signature": [
      "48 54 54 50"
    ],
    "description": "Cascading Style Sheet",
    "mime_type": mime_types.get("css")
  },
  "xml": {
    "hex_signature": [
      "3C 3F 78 6D 6C 20", "3C 00 3F 00 78 00 6D 00 6C 00 20",
      "00 3C 00 3F 00 78 00 6D 00 6C 00 20", "3C 00 00 00 3F 00 00 00 78 00 00 00 6D 00 00 00 6C 00 00 00 20 00 00 00", "00 00 00 3C 00 00 00 3F 00 00 00 78 00 00 00 6D 00 00 00 6C 00 00 00 20", "4C 6F A7 94 93 40"
    ],
    "description": "XML document",
    "mime_type": mime_types.get("xml")
  },
  
  "gif": {
    "hex_signature": [
      "47 49 46 38 37 61", "47 49 46 38 39 61"
    ],
    "description": "GIF image",
    "mime_type": mime_types.get("gif")
  },
  "jpeg": {
    "hex_signature": [
      "FF D8 FF E0 00 10 4A 46 49 46 00 01", "FF D8 FF EE", "FF D8 FF E1 45 78 69 66 00 00",
    ],
    "description": "JPEG image",
    "mime_type": mime_types.get("jpeg")
  },
  "jpg": {
    "hex_signature": [
      "FF D8 FF E0", "FF D8 FF E0 00 10 4A 46 49 46 00 01", "FF D8 FF EE", "FF D8 FF E1 45 78 69 66 00 00",
    ],
    "description": "JPEG image",
    "mime_type": mime_types.get("jpg")
  },
 
  "atom": {
    "hex_signature": [
      "41 6E 64 6F 6D 20 5F 69 6E 6B 20"  
    ],
    "description": "Atom feed",
    "mime_type": mime_types.get("atom")
  },
  "txt": {
    "hex_signature": [
      "EF BB BF",
      "FF FE",
      "FE FF",
      "FF FE 00 00",
      "00 00 FE FF",
      "0E FE FF",
    ],
    "description": "Plain Text File",
    "mime_type": mime_types.get("txt"),
  },
  "png":{
    "hex_signature": [
      "89 50 4E 47 0D 0A 1A 0A",
    ],
    "description": "Image encoded in the Portable Network Graphics format",
    "mime_type": mime_types.get("png")
  },
  "tif": {
    "hex_signature": [
      "49 49 2A 00",
      "4D 4D 00 2A"
    ],
    "description": "Tagged Image File Format (TIFF)",
    "mime_type": mime_types.get("tif")
  },
  "tiff": {
    "hex_signature": ["4D 4D 00 2A"],
    "description": "Tagged Image File Format (TIFF)",
    "mime_type": mime_types.get("tiff")
  },
  "ico": {
    "hex_signature": [
      "00 00 01 00"
    ],
    "description": "Computer icon encoded in ICO file format",
    "mime_type": mime_types.get("ico")
  },
  "bmp": {
    "hex_signature": [
      "42 4D"
    ],
    "description": "BMP file, a bitmap format used mostly in the Windows world",
    "mime_type": mime_types.get("bmp")
  },
  "webp": {
    "hex_signature": [
      "52 49 46 46", "57 45 42 50"
    ],
    
    "description": "File type corresponding to MIME type image/webp",
      "mime_type": mime_types.get("webp")
  },
  "jar": {
    "hex_signature": ["50 4B 03 04", ],
    "description": "Java Archive (JAR) file",
    "mime_type": mime_types.get("jar")
  },
  "doc":{
    "hex_signature": ["D0 CF 11 E0 A1 B1 1A E1"],
    "description": "Microsoft Word document",
    "mime_type": mime_types.get("doc"),
  },
  "pdf": {
    "hex_signature": [
        "25 50 44 46"
    ],
    
    "description": "PDF document",
    "mime_type": mime_types.get("pdf")
  },
  "ps": {
    "hex_signature": [
      "25 21 50 53"
    ],
    
    "description": "PostScript document",
    "mime_type": mime_types.get("ps")
  },
  "eps": {
    "hex_signature": ["25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 30 20 45 50 53 46 2D 33 2E 30", "25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 31 20 45 50 53 46 2D 33 2E 30"],
    "description": "Encapsulated PostScript document",
    "mime_type": mime_types.get("eps")
  },
  "ai": {
    "hex_signature": ["46 4F 52 4D 41 49 46 46", ],
    "description": "Adobe Illustrator document",
    "mime_type": mime_types.get("ai")
  },
  "rtf": {
    "hex_signature": ["7B 5C 72 74 66 31"],
    "description": "Rich Text Format",
    "mime_type": mime_types.get("rtf")
  },
  "xls": {
    "hex_signature": ["D0 CF 11 E0 A1 B1 1A E1"],
    "description": "Microsoft Excel spreadsheet",
    "mime_type": mime_types.get("xls")
  },
  "ppt": {
    "hex_signature": ["D0 CF 11 E0 A1 B1 1A E1"],
    "description": "Microsoft PowerPoint presentation",
    "mime_type": mime_types.get("ppt")
  },
  "kmz": {
    "hex_signature": ["50 4B 03 04"],
    "description": "Google Earth KMZ file",
    "mime_type": mime_types.get("kmz")
  },
  "7z":{
    "hex_signature": ["37 7A BC AF 27 1C"],
    "description": "7-Zip archive",
    "mime_type": mime_types.get("7z")
  },
  "pdb":{
    "hex_signature": ["00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"],
    "description": "PalmPilot Database/Document File",
    "mime_type": mime_types.get("pdb")
  },
  "rar":{
    "hex_signature": ["52 61 72 21 1A 07 01 00"],
    "description": "Roshal ARchive compressed archive",
    "mime_type": mime_types.get("rar")
  },
  "rpm":{
    "hex_signature": ["ED AB EE DB"],
    "description": "RPM Package Manager",
    "mime_type": mime_types.get("rpm")
  },
  "swf":{
    "hex_signature": ["46 57 53"],
    "description": "Adobe Flash .swf",
    "mime_type": mime_types.get("swf")
  },
  "der":{
    "hex_signature": ["30 82"],
    "description": "Distinguished Encoding Rules (DER) encoded certificate",
    "mime_type": mime_types.get("der")
  },
  "pem":{
    "hex_signature": ["2D 2D 2D 2D 2D 42 45 47 49 4E 20 43 45 52 54 49 46 49 43 41 54 45 2D 2D 2D 2D 2D", "2D 2D 2D 2D 2D 42 45 47 49 4E 20 43 45 52 54 49 46 49 43 41 54 45 20 52 45 51 55 45 53 54 2D 2D 2D 2D 2D", "2D 2D 2D 2D 2D 42 45 47 49 4E 20 52 45 41 20 50 52 49 56 41 54 45 20 4B 45 59 2D 2D 2D 2D 2D", ],
    "description": "Privacy Enhanced Mail (PEM) encoded certificate",
    "mime_type": mime_types.get("pem")
  },
  "crt":{
    "hex_signature": ["43 36 34 20 43 41 52 54 52 49 44 47 45 20 20 20"],
    "description": "Commodore 64 cartridge image",
    "mime_type": mime_types.get("crt")
  },
  "xpi":{
    "hex_signature": ["50 4B 03 04"],
    "description": "Mozilla Firefox extension",
    "mime_type": mime_types.get("xpi")
  },
  "zip":{
    "hex_signature": ["50 4B 03 04"],
    "description": "ZIP archive",
    "mime_type": mime_types.get("zip")
  },
  "bin":{
    "hex_signature": ["53 50 30 31"],
    "description": "Binary file or Amazon Kindle Update Package",
    "mime_type": mime_types.get("bin")
  },
  "exe":{
    "hex_signature": ["4D 5A"],
    "description": "Executable file",
    "mime_type": mime_types.get("exe")
  },
  "dll":{
    "hex_signature": ["4D 5A"],
    "description": "Dynamic link library",
    "mime_type": mime_types.get("dll")
  },
  "deb": {
    "hex_signature": ["21 3C 61 72 63 68 3E 0A"],
    "description": "Debian Linux package",
    "mime_type": mime_types.get("deb")
  },
  "dmg": {
    "hex_signature": ["6B 6F 6C 79"],
    "description": "Apple Disk Image",
    "mime_type": mime_types.get("dmg")
  },
  "iso": {
    "hex_signature": ["43 44 30 30 31"],
    "description": "ISO 9660 image",
    "mime_type": mime_types.get("iso"),
  },
  "msi":{
    "hex_signature": ["D0 CF 11 E0 A1 B1 1A E1"],
    "description": "Microsoft Installer package",
    "mime_type": mime_types.get("msi")
  },
  "mid":{
    "hex_signature": ["4D 54 68 64"],
    "description": "MIDI file",
    "mime_type": mime_types.get("mid")
  },
  "midi":{
    "hex_signature": ["4D 54 68 64"],
    "description": "MIDI file",
    "mime_type": mime_types.get("midi"),
  },
  "mp3":{
    "hex_signature": ["FF FB", "FF F3", "FF F2", "49 44 33"],
    "description": "MPEG-1 Audio Layer III file",
    "mime_type": mime_types.get("mp3")
  },
  "ogg": {
    "hex_signature": ["4F 67 67 53"],
    "description": "Ogg Vorbis audio file",
    "mime_type": mime_types.get("ogg")
  },
}
 
