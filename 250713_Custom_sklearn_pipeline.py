# 출처 : https://gist.github.com/dsaint31x/eaa0b0103aaf47b212c20e9cb289e63d 
# 하지만 원본은 완성된 코드가 아니라서 수정하여 코드 완성 

from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.utils.validation import validate_data, check_is_fitted
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.utils.estimator_checks import check_estimator

# scikit-learn 표준화 트랜스포머 커스텀 버전
class StandardScalerClone(TransformerMixin, BaseEstimator):
    def __init__(self, with_mean=True):
        # 생성자: 평균 제거 여부 하이퍼파라미터(기본 True)
        self.with_mean = with_mean

    def fit(self, X, y=None):
        # 학습단계: 평균과 표준편차를 계산해서 저장함
        X_orig = X  # 원본 X(컬럼명 체크용)
        X = validate_data(self, X, reset=True)  # 데이터 정제 및 검증(누락, 차원, 타입 등)
        self.mean_ = X.mean(axis=0)   # 각 특성별 평균값 계산 (numpy or DataFrame 지원)
        self.scale_ = X.std(axis=0)   # 각 특성별 표준편차 계산
        # DataFrame 입력일 때 컬럼명을 특성명으로 저장 (후처리/특성명 지원)
        if hasattr(X_orig, "columns"):
            self.feature_names_in_ = np.array(X_orig.columns, dtype=object)
        return self  # fit은 self 반환 (sklearn 규약)

    def transform(self, X):
        # 변환단계: 입력 데이터를 표준화하여 반환
        check_is_fitted(self)  # fit() 후에만 동작하도록 체크 (안하면 에러)
        X = validate_data(self, X, reset=False)  # 데이터 타입 및 shape 확인
        if self.with_mean:
            X = X - self.mean_  # 평균 제거 (with_mean이 True면)
        return X / self.scale_  # 표준편차로 나누기 (scale_) → 표준화 결과 반환

    def inverse_transform(self, X):
        # 역변환: 표준화된 값을 원래 값으로 복원
        check_is_fitted(self)
        X = validate_data(self, X, reset=False)
        X = X * self.scale_  # 표준편차 곱하기 (스케일 복구)
        return X + self.mean_ if self.with_mean else X  # 평균 더하기(옵션)

    def get_feature_names_out(self, input_features=None):
        # 특성 이름 반환: 입력 특성명 또는 기본명 반환
        if input_features is None:
            # fit시 DataFrame이면 컬럼명, 아니면 기본 "x0", "x1" 반환
            return getattr(self, "feature_names_in_", [f"x{i}" for i in range(self.n_features_in_)])
        else:
            # 입력 특성명 수가 다르면 에러
            if len(input_features) != self.n_features_in_:
                raise ValueError("Invalid number of features")
            # 기존 컬럼명과 입력 특성명이 다르면 에러(일관성 보장)
            if hasattr(self, "feature_names_in_") and not np.all(self.feature_names_in_ == input_features):
                raise ValueError("input_features ≠ feature_names_in_")
            return input_features

# ==================== 사용 예시 ====================

# 1. 예시 데이터 (numpy 2D array)
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# 2. 트랜스포머 인스턴스 생성 (평균 제거 O)
scaler = StandardScalerClone(with_mean=True)

# 3. scikit-learn 표준 평가기 (check_estimator) 통과 확인
print(check_estimator(scaler))  # 에러 없이 동작하면 None 출력

# 4. 파이프라인에 트랜스포머 삽입 (실전 파이프라인 연동 가능)
pipeline = Pipeline([
    ('scaler', scaler)
])

# 5. fit 및 transform: 표준화 수행
pipeline.fit(X)  # 평균/표준편차 저장
X_transformed = pipeline.transform(X)  # 표준화된 데이터 반환
print("Transformed data:\n", X_transformed)

# 6. 역변환: 원본 복원 확인
X_original = pipeline.inverse_transform(X_transformed)
print("Inverse transformed data (original):\n", X_original)

# 7. 특성 이름 반환 테스트 (기본 값)
print("Feature names:", scaler.get_feature_names_out())

# 8. 특성 이름 반환 테스트 (사용자 지정 값)
assert np.all(scaler.get_feature_names_out() == ["x0", "x1"])
assert np.all(scaler.get_feature_names_out(["a", "b"]) == ["a", "b"])

# 9. pandas DataFrame 입력 호환성 체크
df = pd.DataFrame({"a": np.random.rand(100), "b": np.random.rand(100)})
scaler = StandardScalerClone()  # 새 트랜스포머
X_scaled = scaler.fit_transform(df)  # DataFrame도 표준화 정상 동작

# 10. DataFrame 컬럼명 일관성 검증
assert np.all(scaler.feature_names_in_ == ["a", "b"])
assert np.all(scaler.get_feature_names_out() == ["a", "b"])
