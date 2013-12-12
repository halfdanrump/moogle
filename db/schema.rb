# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20131206064554) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"
  enable_extension "pg_trgm"

  create_table "clinics", force: true do |t|
    t.string   "code"
    t.string   "name"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "fulldocs", force: true do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
    t.tsvector "search_vector"
    t.text     "doc"
    t.string   "常勤歯科医師数"
    t.string   "特定機能病院"
    t.string   "開設年月"
    t.string   "特定特別医療法人"
    t.string   "市区郡"
    t.string   "病院日本語名称"
    t.string   "FAX番号"
    t.string   "電話番号"
    t.string   "医療従事者総数"
    t.string   "都道府県"
    t.string   "病院名カナ"
    t.string   "非常勤歯科医師数"
    t.string   "ホームページアドレス"
    t.string   "非常勤医師数"
    t.string   "日本医療機能評価機構認定病院"
    t.string   "経営体"
    t.string   "常勤医師数"
    t.string   "郵便番号"
    t.string   "発行年月日"
    t.string   "住所"
    t.string   "救急告示病院"
    t.string   "地域医療支援"
    t.string   "departments"
    t.string   "machines"
    t.integer  "code"
  end

  add_index "fulldocs", ["code"], name: "index_fulldocs_on_code", unique: true, using: :btree
  add_index "fulldocs", ["doc"], name: "moogle", using: :gist
  add_index "fulldocs", ["search_vector"], name: "fulldocs_search_idx", using: :gin

end
