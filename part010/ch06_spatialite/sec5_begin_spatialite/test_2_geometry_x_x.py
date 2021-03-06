# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
import sqlite3 as sqlite
conn = sqlite.connect("spalite.db")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

################################################################################
sql = '''SELECT ogc_fid, AsText(Geometry) FROM
    hyd2_4l WHERE ogc_fid = 2'''

cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT ogc_fid, NumPoints(Geometry),
  GLength(Geometry), Dimension(Geometry),
  GeometryType(Geometry) FROM hyd2_4l ORDER BY
  NumPoints(Geometry) DESC LIMIT 5'''

cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql = '''SELECT ogc_fid, NumPoints(Geometry),
  AsText(StartPoint(Geometry)), Y(PointN(Geometry, 2))
  FROM hyd2_4l ORDER BY NumPoints(Geometry) DESC LIMIT 5'''

cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql = 'SELECT name, AsText(Geometry) FROM county_popu WHERE ogc_fid = 52'
cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT ogc_fid, Area(Geometry),
    AsText(Centroid(Geometry)),
    Dimension(Geometry), GeometryType(Geometry)
    FROM county_popu
    ORDER BY Area(Geometry) DESC LIMIT 5'''

cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql = '''SELECT ogc_fid, NumInteriorRings(Geometry),
        NumPoints(ExteriorRing(Geometry)),
        NumPoints(InteriorRingN(Geometry, 1))
        FROM county_popu ORDER BY NumInteriorRings(Geometry) DESC LIMIT 5'''

cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql = '''SELECT AsText(InteriorRingN(Geometry, 1)),
    AsText(PointN(InteriorRingN(Geometry, 1), 4)),
    X(PointN(InteriorRingN(Geometry, 1), 5))
    FROM county_popu WHERE ogc_fid = 2364'''

cursor.execute(sql)
cursor.fetchone()
