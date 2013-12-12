class AddJapaneseFulltextIndex < ActiveRecord::Migration
  def change
  	execute <<-SQL
  	  DROP EXTENTION pg_trgm;
      CREATE EXTENSION pg_trgm;
	  CREATE INDEX moogle ON fulldocs USING gist (doc gist_trgm_ops);
    SQL
  end
end
