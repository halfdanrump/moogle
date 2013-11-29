class AddFulltextSearchToFulldocs < ActiveRecord::Migration
  def up
    # 1. Create the search vector column
    add_column :fulldocs, :search_vector, 'tsvector'

    # 2. Create the gin index on the search vector
    execute <<-SQL
      CREATE INDEX fulldocs_search_idx
      ON fulldocs
      USING gin(search_vector);
    SQL

    # 4 (optional). Trigger to update the vector column 
    # when the products table is updated
    execute <<-SQL
      DROP TRIGGER IF EXISTS fulldocs_search_vector_update
      ON fulldocs;
      CREATE TRIGGER fulldocs_search_vector_update
      BEFORE INSERT OR UPDATE
      ON fulldocs
      FOR EACH ROW EXECUTE PROCEDURE
      tsvector_update_trigger (search_vector, 'pg_catalog.english', doc);
    SQL

    Fulldoc.find_each { |p| p.touch }
  end

  def down
    remove_column :fulldocs, :search_vector
    execute <<-SQL
      DROP TRIGGER IF EXISTS fulldocs_search_vector_update on fulldocs;
    SQL
  end
end