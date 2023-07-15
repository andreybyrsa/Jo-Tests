const [alertModal, openAlertModal, closeAlertModal] = useModal(
  "alert-modal",
  null,
  "close-alert-modal-button"
);

if (alertModal) {
  openAlertModal();
}
