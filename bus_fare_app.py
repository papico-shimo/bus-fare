import streamlit as st
import pandas as pd

st.title("バス代集計アプリ")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 列名の前後の空白を除去
    df.columns = df.columns.str.strip()

    # 列名を表示（デバッグ）
    st.write("列名（strip後）:", df.columns.tolist())

    # 必要な列があるか確認
    if "加算か" in df.columns and "実際のバス代金" in df.columns:
        df["加算か"] = df["加算か"].fillna("×")
        df["実際のバス代金"] = pd.to_numeric(df["実際のバス代金"], errors="coerce").fillna(0)

        df_filtered = df[df["加算か"] == "○"]
        total_fare = df_filtered["実際のバス代金"].sum()

        st.write("🚍 加算対象の合計バス代金：", int(total_fare), "円")
        st.dataframe(df_filtered)
    else:
        st.error("❌ 列名『加算か』『実際のバス代金』が見つかりません。CSVのヘッダーを確認してください。")