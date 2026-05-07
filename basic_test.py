import duckdb
con = duckdb.connect("ipeds.duckdb")
con.sql("SELECT * FROM v_institutions LIMIT 10").show()