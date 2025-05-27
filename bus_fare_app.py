st.write("列名リスト（デバッグ用）:", df.columns.tolist())

import streamlit as st
import pandas as pd

st.title("バス代集計アプリ")

# CSVファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    # CSV読み込み
    df = pd.read_csv(uploaded_file)

    # 列名表示（デバッグ用・必要なら表示）
    st.write("列名：", df.columns.tolist())

    # 欠損値処理
    df["加算か"] = df["加算か"].fillna("×")
    df["実際のバス代金"] = df["実際のバス代金"].fillna(0)

    # 数値に変換
    df["実際のバス代金"] = pd.to_numeric(df["実際のバス代金"], errors="coerce").fillna(0)

    # 加算対象の抽出
    df_filtered = df[df["加算か"] == "○"]

    # 合計金額の計算
    total_fare = df_filtered["実際のバス代金"].sum()

    # 表示
    st.write("🚍 加算対象の合計バス代金：", int(total_fare), "円")
    st.dataframe(df_filtered)