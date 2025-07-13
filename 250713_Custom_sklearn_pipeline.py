# 출처 : https://gist.github.com/dsaint31x/eaa0b0103aaf47b212c20e9cb289e63d 
# 하지만 수정이 필요했음 

from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.utils.validation import validate_data, check_is_fitted
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.utils.estimator_checks import check_estimator

class StandardScalerClone(TransformerMixin, BaseEstimator):
    def __init__(self, with_mean=True):
        self.with_mean = with_mean

    def fit(self, X, y=None):
        X_orig = X
        X = validate_data(self, X, reset=True)
        self.mean_ = X.mean(axis=0)
        self.scale_ = X.std(axis=0)
        if hasattr(X_orig, "columns"):
            self.feature_names_in_ = np.array(X_orig.columns, dtype=object)
        return self

    def transform(self, X):
        check_is_fitted(self)
        X = validate_data(self, X, reset=False)
        if self.with_mean:
            X = X - self.mean_
        return X / self.scale_

    def inverse_transform(self, X):
        check_is_fitted(self)
        X = validate_data(self, X, reset=False)
        X = X * self.scale_
        return X + self.mean_ if self.with_mean else X

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            return getattr(self, "feature_names_in_", [f"x{i}" for i in range(self.n_features_in_)])
        else:
            if len(input_features) != self.n_features_in_:
                raise ValueError("Invalid number of features")
            if hasattr(self, "feature_names_in_") and not np.all(self.feature_names_in_ == input_features):
                raise ValueError("input_features ≠ feature_names_in_")
            return input_features

# 예시 데이터 생성
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# 트랜스포머 초기화
scaler = StandardScalerClone(with_mean=True)

# check_estimator 통과
print(check_estimator(scaler))  # 에러 없이 동작

# 파이프라인에 적용
pipeline = Pipeline([
    ('scaler', scaler)
])

# 데이터 학습 및 변환
pipeline.fit(X)
X_transformed = pipeline.transform(X)
print("Transformed data:\n", X_transformed)

# 역변환
X_original = pipeline.inverse_transform(X_transformed)
print("Inverse transformed data (original):\n", X_original)

# 특성 이름 출력
print("Feature names:", scaler.get_feature_names_out())

# 특성 이름 동작을 좀더 확인.
assert np.all(scaler.get_feature_names_out() == ["x0", "x1"])
assert np.all(scaler.get_feature_names_out(["a", "b"]) == ["a", "b"])

# DataFrame과 잘 동작하나?
df = pd.DataFrame({"a": np.random.rand(100), "b": np.random.rand(100)})
scaler = StandardScalerClone()
X_scaled = scaler.fit_transform(df)

assert np.all(scaler.feature_names_in_ == ["a", "b"])
assert np.all(scaler.get_feature_names_out() == ["a", "b"])
