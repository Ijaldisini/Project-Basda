CREATE TABLE Akun 
    ( 
     id_akun SERIAL  NOT NULL , 
     no_hp   VARCHAR (12)  NOT NULL , 
     nama    VARCHAR (50)  NOT NULL , 
     Role    VARCHAR (10) NOT NULL 
    ) 
;

ALTER TABLE Akun 
    ADD CONSTRAINT Akun_PK PRIMARY KEY ( id_akun ) ;

ALTER TABLE Akun 
    ADD CONSTRAINT Akun_no_hp_UN UNIQUE ( no_hp ) ;

CREATE TABLE Bibit_Tanaman 
    ( 
     id_bibit             SERIAL  NOT NULL , 
     nama_bibit           VARCHAR (30)  NOT NULL , 
     stok                 INTEGER  NOT NULL , 
     usia_panen           INTEGER  NOT NULL , 
     hasil_panen_perbibit INTEGER  NOT NULL , 
     harga_perkg          INTEGER  NOT NULL , 
     harga_bibit          INTEGER  NOT NULL , 
     Panen_id_panen       INTEGER 
    ) 
;

ALTER TABLE Bibit_Tanaman 
    ADD CONSTRAINT Bibit_Tanaman_PK PRIMARY KEY ( id_bibit ) ;

CREATE TABLE Detail_Nutrisi 
    ( 
     id_detail_nutrisi      SERIAL  NOT NULL , 
     Dosis                  INTEGER  NOT NULL , 
     Bibit_Tanaman_id_bibit INTEGER  NOT NULL , 
     Nutrisi_id_nutrisi     INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Detail_Nutrisi 
    ADD CONSTRAINT Detail_Nutrisi_PK PRIMARY KEY ( id_detail_nutrisi ) ;

CREATE TABLE Detail_Penyakit 
    ( 
     id_detail_penyakit   SERIAL  NOT NULL , 
     Gejala_id_gejala     INTEGER  NOT NULL , 
     Penyakit_id_penyakit INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Detail_Penyakit 
    ADD CONSTRAINT Detail_Penyakit_PK PRIMARY KEY ( id_detail_penyakit ) ;

CREATE TABLE Detail_Transaksi 
    ( 
     id_detail_transaksi    SERIAL  NOT NULL , 
     Jumlah                 INTEGER  NOT NULL , 
     nominal                INTEGER  NOT NULL , 
     Transaksi_id_transaksi INTEGER  NOT NULL , 
     Panen_id_panen         INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Detail_Transaksi 
    ADD CONSTRAINT Detail_Transaksi_PK PRIMARY KEY ( id_detail_transaksi ) ;

CREATE TABLE Gejala 
    ( 
     id_gejala SERIAL  NOT NULL , 
     gejala    VARCHAR (50)  NOT NULL 
    ) 
;

ALTER TABLE Gejala 
    ADD CONSTRAINT Gejala_PK PRIMARY KEY ( id_gejala ) ;

CREATE TABLE Nutrisi 
    ( 
     id_nutrisi   SERIAL  NOT NULL , 
     nama_nutrisi VARCHAR (30)  NOT NULL 
    ) 
;

ALTER TABLE Nutrisi 
    ADD CONSTRAINT Nutrisi_PK PRIMARY KEY ( id_nutrisi ) ;

CREATE TABLE Panen 
    ( 
     id_panen          SERIAL  NOT NULL , 
     tanggal_tanam     DATE  NOT NULL , 
     tanggal_panen     DATE  NOT NULL , 
     batas_panen       DATE  NOT NULL , 
     total_hasil_panen INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Panen 
    ADD CONSTRAINT Panen_PK PRIMARY KEY ( id_panen ) ;

CREATE TABLE Penyakit 
    ( 
     id_penyakit    SERIAL  NOT NULL , 
     nama_penyakit  VARCHAR (30)  NOT NULL , 
     penanganan     TEXT  NOT NULL , 
     Panen_id_panen INTEGER 
    ) 
;

ALTER TABLE Penyakit 
    ADD CONSTRAINT Penyakit_PK PRIMARY KEY ( id_penyakit ) ;

CREATE TABLE Rak_Budidaya 
    ( 
     id_rak         SERIAL  NOT NULL , 
     bibit_per_rak  INTEGER  NOT NULL , 
     Panen_id_panen INTEGER 
    ) 
;

ALTER TABLE Rak_Budidaya 
    ADD CONSTRAINT Rak_Budidaya_PK PRIMARY KEY ( id_rak ) ;

CREATE TABLE Transaksi 
    ( 
     id_transaksi SERIAL  NOT NULL , 
     tanggal      DATE  NOT NULL , 
     Akun_id_akun INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Transaksi 
    ADD CONSTRAINT Transaksi_PK PRIMARY KEY ( id_transaksi ) ;

ALTER TABLE Bibit_Tanaman 
    ADD CONSTRAINT Bibit_Tanaman_Panen_FK FOREIGN KEY 
    ( 
     Panen_id_panen
    ) 
    REFERENCES Panen 
    ( 
     id_panen
    ) 
;

ALTER TABLE Detail_Nutrisi 
    ADD CONSTRAINT Dtl_Nutrsi_Bbt_Tnman_FK FOREIGN KEY 
    ( 
     Bibit_Tanaman_id_bibit
    ) 
    REFERENCES Bibit_Tanaman 
    ( 
     id_bibit
    ) 
;

ALTER TABLE Detail_Nutrisi 
    ADD CONSTRAINT Detail_Nutrisi_Nutrisi_FK FOREIGN KEY 
    ( 
     Nutrisi_id_nutrisi
    ) 
    REFERENCES Nutrisi 
    ( 
     id_nutrisi
    ) 
;

ALTER TABLE Detail_Penyakit 
    ADD CONSTRAINT Detail_Penyakit_Gejala_FK FOREIGN KEY 
    ( 
     Gejala_id_gejala
    ) 
    REFERENCES Gejala 
    ( 
     id_gejala
    ) 
;

ALTER TABLE Detail_Penyakit 
    ADD CONSTRAINT Detail_Penyakit_Penyakit_FK FOREIGN KEY 
    ( 
     Penyakit_id_penyakit
    ) 
    REFERENCES Penyakit 
    ( 
     id_penyakit
    ) 
;

ALTER TABLE Detail_Transaksi 
    ADD CONSTRAINT Detail_Transaksi_Panen_FK FOREIGN KEY 
    ( 
     Panen_id_panen
    ) 
    REFERENCES Panen 
    ( 
     id_panen
    ) 
;

ALTER TABLE Detail_Transaksi 
    ADD CONSTRAINT Detail_Transaksi_Transaksi_FK FOREIGN KEY 
    ( 
     Transaksi_id_transaksi
    ) 
    REFERENCES Transaksi 
    ( 
     id_transaksi
    ) 
;

ALTER TABLE Penyakit 
    ADD CONSTRAINT Penyakit_Panen_FK FOREIGN KEY 
    ( 
     Panen_id_panen
    ) 
    REFERENCES Panen 
    ( 
     id_panen
    ) 
;

ALTER TABLE Rak_Budidaya 
    ADD CONSTRAINT Rak_Budidaya_Panen_FK FOREIGN KEY 
    ( 
     Panen_id_panen
    ) 
    REFERENCES Panen 
    ( 
     id_panen
    ) 
;

ALTER TABLE Transaksi 
    ADD CONSTRAINT Transaksi_Akun_FK FOREIGN KEY 
    ( 
     Akun_id_akun
    ) 
    REFERENCES Akun 
    ( 
     id_akun
    ) 
;



