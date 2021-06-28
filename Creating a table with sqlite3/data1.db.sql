BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Ogrenciler" (
	"OgrNo"	,
	"Ad"	,
	"Soyad"	
);
CREATE TABLE IF NOT EXISTS "Dersler" (
	"DersKodu"	,
	"DersAdı"	
);
CREATE TABLE IF NOT EXISTS "Notlar" (
	"OgrNo"	,
	"DersKodu"	,
	"Vize"	,
	"Final"	
);
CREATE TABLE IF NOT EXISTS "Personel" (
	"PerNo"	,
	"Ad"	,
	"Soyad"	
);
INSERT INTO "Ogrenciler" VALUES ('123456789','Selim','Solmaz');
INSERT INTO "Ogrenciler" VALUES ('987654321','Ali','Çınar');
INSERT INTO "Ogrenciler" VALUES ('231564321','Songül','Tahmaz');
INSERT INTO "Dersler" VALUES ('BIL107','Bilgisayar Programlama');
INSERT INTO "Dersler" VALUES ('BIL117','Temel Bilgi Teknolojileri');
INSERT INTO "Dersler" VALUES ('BIL121','Programlama Dillerine Giriş');
INSERT INTO "Notlar" VALUES ('231564321','BIL107','50','70');
INSERT INTO "Notlar" VALUES ('123456789','BIL107','70','80');
INSERT INTO "Notlar" VALUES ('123456789','BIL117','70','45');
INSERT INTO "Notlar" VALUES ('231564321','BIL117','56','87');
INSERT INTO "Notlar" VALUES ('987654321','BIL117','70','76');
INSERT INTO "Personel" VALUES ('101','Ali','Solmaz');
INSERT INTO "Personel" VALUES ('102','Altan','Solmaz');
INSERT INTO "Personel" VALUES ('103','Altan','Mesut');
INSERT INTO "Personel" VALUES ('222','dsd','fdfs');
INSERT INTO "Personel" VALUES ('222','dsd','fdfs');
INSERT INTO "Personel" VALUES ('222','dsd','fdfs');
COMMIT;
