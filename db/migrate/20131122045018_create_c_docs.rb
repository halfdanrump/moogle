class CreateCDocs < ActiveRecord::Migration
  def change
    create_table :c_docs do |t|
      t.integer :code
      t.text :doc

      t.timestamps
    end
  end
end
